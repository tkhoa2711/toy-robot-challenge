# ADR 1: Initial design and project layout

## Context

We want to decide on the design of our application, and that will also influence
the project layout i.e. how we structure our source code.

## Decision

The project core domain evolves around the robot and its position on the table.
We will model those concepts as the core of our application.

The way users are going to interact with the application is via a console. That
shall be abstracted into its own module that will be encapsulated from how the
core domain logic works. Imagine the console is just a special type of UI such
that we can swap it out with a real GUI later if needed.

We also need a way to store the current state of the user "session". We decide
to implement a `State` module who is responsible to manage the state of the app,
which at this stage just contains the table and the robot's position.

Overall, the project layout will contain the following components:

* Domain
* UI/Console
* State

## Status

Accepted

## Consequences

Pros:

* Clear separation of responsibility for each module
* Simple enough to get us started without introducing complexity prematurely
* Easy to extend in the future if need be

Cons:

* The domain model may evolve unexpectedly that we would have to re-model the
  whole thing
