# The Move Book

Address is a unique identifier of a location on the blockchain. It is used to identify
 [packages](./packages.html) ,  [accounts](./what-is-an-account.html) , and  [objects](./object-storage.html) .
Address has a fixed size of 32 bytes and is usually represented as a hexadecimal string prefixed
with  0x . Addresses are case insensitive.

The address above is an example of a valid address. It is 64 characters long (32 bytes) and prefixed
with  0x .

Sui also has reserved addresses that are used to identify standard packages and objects. Reserved
addresses are typically simple values that are easy to remember and type. For example, the address
of the Standard Library is  0x1 . Addresses, shorter than 32 bytes, are padded with zeros to the
left.

Here are some examples of reserved addresses:

You can find all reserved addresses in the  [Appendix B](../appendix/reserved-addresses.html) .

## Further reading