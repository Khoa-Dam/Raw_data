# The Move Book

The Move Standard Library provides functionality for native types and operations. It is a standard
collection of modules that do not interact with storage, but provide basic tools for working with
and manipulating data. It is the only dependency of the
 [Sui Framework](../programmability/sui-framework.html) , and is imported together with it.

In this book we go into detail about most of the modules in the Standard Library, however, it is
also helpful to give an overview of the features, so that you can get a sense of what is available
and which module implements it.

The Move Standard Library provides a set of functions associated with integer types. These functions
are split into multiple modules, each associated with a specific integer type. The modules should
not be imported directly, as their functions are available on every integer value.

All of the modules provide the same set of functions. Namely,  max ,  diff ,
 divide_and_round_up ,  sqrt  and  pow .

The Standard Library exports a single named address -  std = 0x1 . Note the alias  std  is defined here.

Some modules are imported implicitly and are available in the module without the explicit  use 
import. For the Standard Library, these modules and types include:

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Most Common Modules

In this book we go into detail about most of the modules in the Standard Library, however, it is
also helpful to give an overview of the features, so that you can get a sense of what is available
and which module implements it.

The Move Standard Library provides a set of functions associated with integer types. These functions
are split into multiple modules, each associated with a specific integer type. The modules should
not be imported directly, as their functions are available on every integer value.

All of the modules provide the same set of functions. Namely,  max ,  diff ,
 divide_and_round_up ,  sqrt  and  pow .

The Standard Library exports a single named address -  std = 0x1 . Note the alias  std  is defined here.

```bash
[addresses]
std = "0x1"
```

Some modules are imported implicitly and are available in the module without the explicit  use 
import. For the Standard Library, these modules and types include:

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

```bash
MoveStdlib = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework/packages/move-stdlib", rev = "framework/mainnet" }
```

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Integer Modules

The Move Standard Library provides a set of functions associated with integer types. These functions
are split into multiple modules, each associated with a specific integer type. The modules should
not be imported directly, as their functions are available on every integer value.

All of the modules provide the same set of functions. Namely,  max ,  diff ,
 divide_and_round_up ,  sqrt  and  pow .

The Standard Library exports a single named address -  std = 0x1 . Note the alias  std  is defined here.

```bash
[addresses]
std = "0x1"
```

Some modules are imported implicitly and are available in the module without the explicit  use 
import. For the Standard Library, these modules and types include:

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

```bash
MoveStdlib = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework/packages/move-stdlib", rev = "framework/mainnet" }
```

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Exported Addresses

The Standard Library exports a single named address -  std = 0x1 . Note the alias  std  is defined here.

```bash
[addresses]
std = "0x1"
```

Some modules are imported implicitly and are available in the module without the explicit  use 
import. For the Standard Library, these modules and types include:

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

```bash
MoveStdlib = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework/packages/move-stdlib", rev = "framework/mainnet" }
```

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Implicit Imports

Some modules are imported implicitly and are available in the module without the explicit  use 
import. For the Standard Library, these modules and types include:

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

```bash
MoveStdlib = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework/packages/move-stdlib", rev = "framework/mainnet" }
```

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Importing std without Sui Framework

The Move Standard Library can be imported to the package directly. However,  std  alone is not
enough to build a meaningful application, as it does not provide any storage capabilities and can't
interact with the on-chain state.

```bash
MoveStdlib = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework/packages/move-stdlib", rev = "framework/mainnet" }
```

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .

## Source Code

The source code of the Move Standard Library is available in the
 [Sui repository](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/move-stdlib/sources) .