# Python fundamentals · Practice notes

A learning collection of small Python exercises and annotated examples covering strings,
numeric operations, built-in collections, type conversion, and conditional logic.
The original Russian comments and exercise text are preserved.

**Status:** educational source archive, with both runnable examples and unfinished notes.
It is not presented as a deployed service, an automated test suite, or a production library.

## Contents

| File | Topic / current role |
| --- | --- |
| [Task2.py](Task2.py) | Arithmetic, storage-size calculations, strings, and geometry exercises |
| [Task3.py](Task3.py) | Type conversion and a short interactive string-length prompt |
| [Task4.py](Task4.py) | Collection notes; currently contains a syntax error |
| [Task6.py](Task6.py) | Membership, divisibility, and conditional expressions |
| [Test 1.py](Test%201.py) | Greeting example and assignments of built-in Python types |
| [Test4.py](Test4.py) | Tuple / dictionary notes, including exception-producing examples |
| [task1.py](task1.py) | String-operation notes; currently contains syntax errors |
| [task5.py](task5.py) | Lists, indexing, sets, dictionaries, and deduplication exercises |
| [task7.py](task7.py) | Conditional-logic drafts; currently contains syntax errors |
| [test6.py](test6.py) | Boolean / branch examples; later statements refer to undefined `a` |

Filenames and case are retained to preserve the original collection.

## Run an example

Use Python 3. The verification environment for this documentation pass was Python 3.13.3.
From the repository root:

```sh
python "Test 1.py"
python Task6.py
python task5.py
```

These three scripts were executed successfully during the documentation pass.
`python Task3.py` starts an interactive example and asks for a string.
There are no third-party dependencies or installation steps.

## Reading the notes

Treat each topic as a separate exercise. Some files intentionally demonstrate operations
that raise exceptions, while others contain unfinished syntax or logical mistakes.
For example, tuple mutation in `Test4.py` raises `TypeError`; the square calculation in
`Task2.py` uses `^` (XOR) instead of exponentiation. These existing behaviors are documented,
not changed by this presentation update.

Files with names beginning `Test` are learning notes, not pytest or unittest cases.
There is no repository-wide application entrypoint or deployment configuration.

## Verification and next steps

- Syntax is checked independently from execution, so interactive input is not required.
- Existing syntax problems in `Task4.py`, `task1.py`, and `task7.py` remain visible.
- Smoke execution is limited to the three self-contained examples listed above.
- A follow-up learning task can separate intentional error demonstrations, repair unfinished
  examples, and add assertions around the expected results.

This README makes the collection navigable without upgrading its maturity claims.
A repository license file has not been supplied.
