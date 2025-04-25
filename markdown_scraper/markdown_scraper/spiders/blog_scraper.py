import scrapy
import os
import re
from urllib.parse import urljoin
import markdown as md
import pdfkit

class BlogScraperSpider(scrapy.Spider):
    name = "blog_scraper"
    allowed_domains = ["move-book.com"]
    start_urls = ["https://move-book.com/"]
    visited_urls = set()

    def parse(self, response):
        sidebar_links = response.css('nav#sidebar a::attr(href)').getall()
        for link in sidebar_links:
            absolute_url = urljoin(response.url, link)
            if absolute_url not in self.visited_urls:
                self.visited_urls.add(absolute_url)
                yield response.follow(absolute_url, callback=self.parse_page)

        yield from self.parse_page(response)

    def parse_page(self, response):
        title = response.css('h1::text').get()
        if not title:
            title = "untitled"

        markdown_content = f"# {title}\n\n"
        paragraphs = response.css('main p')
        for p in paragraphs:
            text = p.css('::text').getall()
            links = p.css('a')
            if links:
                for link in links:
                    link_text = link.css('::text').get()
                    link_href = link.css('::attr(href)').get()
                    for i, t in enumerate(text):
                        if t == link_text:
                            text[i] = f"[{link_text}]({link_href})"
            markdown_content += " ".join(text).strip() + "\n\n"

        sections = response.css('main h2')
        for section in sections:
            subtitle = section.css('::text').get()
            if subtitle:
                markdown_content += f"## {subtitle}\n\n"

            next_elements = section.xpath('following-sibling::*[not(self::h2)]')
            for elem in next_elements:
                paragraphs = elem.css('p')
                for p in paragraphs:
                    text = p.css('::text').getall()
                    links = p.css('a')
                    if links:
                        for link in links:
                            link_text = link.css('::text').get()
                            link_href = link.css('::attr(href)').get()
                            for i, t in enumerate(text):
                                if t == link_text:
                                    text[i] = f"[{link_text}]({link_href})"
                    markdown_content += " ".join(text).strip() + "\n\n"

                code = elem.css('pre code::text').get()
                if code:
                    markdown_content += "```bash\n" + code.strip() + "\n```\n\n"

        filename = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').lower()
        filename = f"{filename}_{re.sub(r'[^\w]', '_', response.url.split('/')[-1])}"

        output_dir = "output_pdf"  # Change output directory name
        os.makedirs(output_dir, exist_ok=True)

        # Convert markdown to HTML directly (without saving file)
        html_content = md.markdown(markdown_content)

        # Convert HTML to PDF
        try:
            config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
            
            options = {
                'encoding': 'UTF-8',
                'enable-local-file-access': None,
                'quiet': None,
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in'
            }
            
            pdf_path = os.path.join(output_dir, f"{filename}.pdf")
            pdfkit.from_string(
                html_content, 
                pdf_path, 
                configuration=config, 
                options=options
            )
            self.log(f"✅ PDF file saved successfully: {pdf_path}")
        except Exception as e:
            self.log(f"❌ Error when converting to PDF: {e}")
            self.log("Please make sure wkhtmltopdf is installed correctly")
