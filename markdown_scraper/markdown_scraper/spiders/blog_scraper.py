import scrapy
import os
import re
from urllib.parse import urljoin

class BlogScraperSpider(scrapy.Spider):
    name = "blog_scraper"
    allowed_domains = ["move-book.com"]
    start_urls = ["https://move-book.com/"]
    visited_urls = set()  # Theo dõi URL đã cào để tránh lặp

    def parse(self, response):
        # Trích xuất tất cả liên kết từ sidebar
        sidebar_links = response.css('nav#sidebar a::attr(href)').getall()
        for link in sidebar_links:
            absolute_url = urljoin(response.url, link)
            if absolute_url not in self.visited_urls:
                self.visited_urls.add(absolute_url)
                yield response.follow(absolute_url, callback=self.parse_page)

        # Cào trang chính luôn
        yield from self.parse_page(response)

    def parse_page(self, response):
        # Lấy tiêu đề chính từ h1
        title = response.css('h1::text').get()
        if not title:
            title = "untitled"

        # Tạo nội dung Markdown
        markdown_content = f"# {title}\n\n"

        # Lấy nội dung từ các thẻ <p> trong <main> và xử lý link
        paragraphs = response.css('main p')
        for p in paragraphs:
            # Lấy văn bản thô
            text = p.css('::text').getall()
            # Xử lý các liên kết <a>
            links = p.css('a')
            if links:
                for link in p.css('a'):
                    link_text = link.css('::text').get()
                    link_href = link.css('::attr(href)').get()
                    # Thay văn bản thô bằng định dạng Markdown [text](href)
                    for i, t in enumerate(text):
                        if t == link_text:
                            text[i] = f"[{link_text}]({link_href})"
            markdown_content += " ".join(text).strip() + "\n\n"

        # Lấy các tiêu đề phụ (h2) và nội dung liên quan
        sections = response.css('main h2')
        for section in sections:
            subtitle = section.css('::text').get()
            if subtitle:
                markdown_content += f"## {subtitle}\n\n"

            next_elements = section.xpath('following-sibling::*[not(self::h2)]')
            for elem in next_elements:
                # Văn bản trong <p> với link
                paragraphs = elem.css('p')
                for p in paragraphs:
                    text = p.css('::text').getall()
                    links = p.css('a')
                    if links:
                        for link in p.css('a'):
                            link_text = link.css('::text').get()
                            link_href = link.css('::attr(href)').get()
                            for i, t in enumerate(text):
                                if t == link_text:
                                    text[i] = f"[{link_text}]({link_href})"
                    markdown_content += " ".join(text).strip() + "\n\n"

                # Mã lệnh trong <pre><code>
                code = elem.css('pre code::text').get()
                if code:
                    markdown_content += "```bash\n" + code.strip() + "\n```\n\n"

        # Tạo tên file từ tiêu đề chính và URL để tránh trùng
        filename = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').lower()
        filename = f"{filename}_{re.sub(r'[^\w]', '_', response.url.split('/')[-1])}.md"

        # Tạo thư mục lưu file
        output_dir = "output_markdown"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Ghi vào file Markdown
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
            f.write(markdown_content.strip())
        self.log(f"Saved file: {filename}")