# Style #10

## Constraints:

* Existence of an abstraction to which values can be converted.
* This abstraction provides operations to (1) wrap around values, so that they become the abstraction; (2) bind itself to functions, so to establish sequences of functions; and (3) unwrap the value, so to examine the final result.
* Larger problem is solved as a pipeline of functions bound together, with unwrapping happening at the end.
* Particularly for The One style, the bind operation simply calls the given function, giving it the value that it holds, and holds on to the returned value.

## Possible names:

* The One
* Monadic Identity
* The wrapper of all things
* Imperative functional style

# Style #11

## Constraints:

* The larger problem is decomposed into 'things' that make sense for the problem domain
* Each 'thing' is a capsule of data that exposes procedures to the rest of the world
* Data is never accessed directly, only through these procedures
* Capsules can reappropriate procedures defined in other capsules

## Possible names:

* Things
* Object-oriented style
* The Kingdom of Nouns (http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html)
