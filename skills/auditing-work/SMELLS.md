# Smell Baseline

A fixed set of code smells the Standards helper looks for even when the project documents no rules of its own. Two rules bind it:

- **The project overrides.** A rule in `.vibe/STANDARDS.md` always wins; where it allows something below, skip that smell.
- **Always a judgement call.** Each smell is a labelled hint ("possible Envious Function"), never a hard violation.

Each reads _what it is_ → _the usual fix_. Match it against the diff.

- **Hidden Name**: a function, value, or file whose name does not say what it does or holds. → Rename it, using `.vibe/WORDS.md` where a word fits; if no honest name comes, the design is muddy.
- **Copy-Paste**: the same logic appears in more than one place in the change. → Pull out the shared shape and call it from both.
- **Envious Function**: a function that works on another module's data more than its own. → Move it next to the data it uses.
- **Travelling Pack**: the same few values keep being passed around together. → Bundle them into one named thing.
- **Bare Text for a Real Thing**: a plain string or number stands in for a concept with a name in the wordbook (a Booking id, a price). → Give the concept its own small type.
- **Repeated Branching**: the same `if`/`switch` on the same kind of thing recurs across the change. → One lookup both places share.
- **Scattered Edit**: one change to behaviour forced small edits across many files. → Gather what changes together into one module.
- **Many-Job File**: one file was edited for several unrelated reasons. → Split it so each file changes for one reason.
- **Just In Case**: options, settings, or layers added for needs the plan does not have. → Delete it until a real need appears.
- **Long Reach**: code walks a long chain of other modules' insides (`a.b().c().d()`). → Hide the walk behind one function on the first module.
- **Pass-Through**: a function or module that only hands work onward. → Call the real target directly.
- **Shallow Module**: a module whose interface is nearly as big as what it hides. → Merge it into its caller, or deepen it so a small interface hides real work.
