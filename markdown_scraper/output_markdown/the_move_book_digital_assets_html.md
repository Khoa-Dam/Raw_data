# The Move Book

Smart-contract programming languages have historically focused on defining and managing digital
assets. For example, the ERC-20 standard in Ethereum pioneered a set of standards to interact with
digital currency tokens, establishing a blueprint for creating and managing digital currencies on
the blockchain. Subsequently, the introduction of the ERC-721 standard marked a significant
evolution, popularizing the concept of non-fungible tokens (NFTs), which represent unique,
indivisible assets. These standards laid the groundwork for the complex digital assets we see today.

However, Ethereum's programming model lacked a native representation of assets. In other words,
externally, a Smart Contract behaved like an asset, but the language itself did not have a way to
inherently represent assets. From the start, Move aimed to provide a first-class abstraction for
assets, opening up new avenues for thinking about and programming assets.

It is important to highlight which properties are essential for an asset:

Ownership:  Every asset is associated with an owner(s), mirroring the straightforward concept
of ownership in the physical world—just as you own a car, you can own a digital asset. Move
enforces ownership in such a way that once an asset is  moved , the previous owner completely
loses any control over it. This mechanism ensures a clear and secure change of ownership.

Non-copyable:  In the real world, unique items cannot be duplicated effortlessly. Move applies
this principle to digital assets, ensuring they cannot be arbitrarily copied within the program.
This property is crucial for maintaining the scarcity and uniqueness of digital assets, mirroring
the intrinsic value of physical assets.

Non-discardable:  Just as you cannot accidentally lose a house or a car without a trace, Move
ensures that no asset can be discarded or lost in a program. Instead, assets must be explicitly
transferred or destroyed. This property guarantees the deliberate handling of digital assets,
preventing accidental loss and ensuring accountability in asset management.

Move managed to encapsulate these properties in its design, becoming an ideal language for digital
assets.

## Summary

## Further reading