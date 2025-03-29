# The Move Book

The  drop  ability - the simplest of them - allows the instance of a struct to be  ignored  or
 discarded . In many programming languages this behavior is considered default. However, in Move, a
struct without the  drop  ability is not allowed to be ignored. This is a safety feature of the Move
language, which ensures that all assets are properly handled. An attempt to ignore a struct without
the  drop  ability will result in a compilation error.

The  drop  ability is often used on custom collection types to eliminate the need for special
handling of the collection when it is no longer needed. For example, a  vector  type has the  drop 
ability, which allows the vector to be ignored when it is no longer needed. However, the biggest
feature of Move's type system is the ability to not have  drop . This ensures that the assets are
properly handled and not ignored.

A struct with a single  drop  ability is called a  Witness . We explain the concept of a  Witness 
in the
 [Witness and Abstract Implementation](./../programmability/witness-pattern.html) 
section.

All native types in Move have the  drop  ability. This includes:

All of the types defined in the standard library have the  drop  ability as well. This includes:

## Types with the 

All native types in Move have the  drop  ability. This includes:

All of the types defined in the standard library have the  drop  ability as well. This includes:

## Further reading