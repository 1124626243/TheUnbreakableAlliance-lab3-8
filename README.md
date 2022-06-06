# TheUnbreakableAlliance-lab3-8

This is lab3 report.

## Variant

(8) S-expression machine with global context

## laboratory work description

- You need to implement simple Lisp-like language with the following construction:

> >     – <expression> ::= <number> | <var-name> | <fun-call>
>  >
>  >       – <number> ::= 1 | 2 | ...
>   >
>   >       – <var-name> ::= a, b, ...
>   >
>   >       – <fun-call> ::= (<fun-or-statement-name> <expression> <expression> ...)
>   >
>   >       – (set <var-name> <expression>) – set variable value
>   >
>   >       – (if <expression> <if-true-expression>
>   >       <if-false-expression>), use 0 for false, and non-zero value for true
>   >
>   >       – (progn <expression> <expression> ...) – evaluate sequence of expression
>   >
>   >       – (while <expression> <expression> <expression> ...)
>   >       – evaluate sequence of expression
>   >
>   >       – functions: print, +, -, +, /, =, <, >, and, or, not.

- Variables storing in one global context.
- Run-time error should be processed correctly.
- You should use the default Python logging module to make the interpreter work transparent

## Project structure

- `discrete_event.py` -- implementation of S-expression machine with global context.
- `discrete_event_test.py` -- unit and PBT tests for `discrete_event.py`.

## Contribution

- Fan Yuxin (1124626243@qq.com) -- discrete_event.py
- Wen Wenchao(285404190@qq.com) -- test.py

## Changelog

- 06.06.2022-3
- Fan Yuxin uploaded `discrete_event_test.py`.
- 05.06.2022 - 2
- Wen Wenchao uploaded `discrete_event_test.py`.
- 05.06.2022 - 1
- Fan Yuxin uploaded `discrete_event.py`.
- 05.06.2022 - 0
  - Initial

## Design notes

We implement simple Lisp-like language:S-expression machine with global context
