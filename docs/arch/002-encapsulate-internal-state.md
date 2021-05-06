# ADR 2: Encapsulate internal state from user-facing interface

## Context

The current implementation of the `console` module has too much knowledge about the internals of the `state`. Each
action it performs needs to access either the `table` or the `robot`.

## Decision

We will extract those user actions into their own module which encapsulates the internal state of the application. The
Console now only needs to know which action to invoke depending on user input.

Then we would have a nice separation of concerns for each module:

```
      interact with            perform           update
User ---------------> Console ---------> Action --------> State
```

This sounds very much similar to the [Elm architecture](https://guide.elm-lang.org/architecture/) used as a pattern for
designing interactive programs. This design takes inspiration from the Elm architecture and then simplifies it to make
it more applicable to the current state of our application.

## Status

Accepted

## Consequences

Pros:

* Encapsulate the internal state from user interactions
* Not complicating the design too much at this early stage

Cons:
