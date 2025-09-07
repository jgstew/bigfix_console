# bigfix_console
A BigFix console console. A BigFix interactive console program written in Python using Textual.


## BigFix Action Type Logic Truth Table
This table maps the possible boolean combinations of BigFix Action properties to a specific Action Type.

| multiple flag | offer flag | exists source fixlet | Resulting Action Type |
| -------- | ------- | ------- | ------- |
| false | false | false | Action |
| false | false | true | Action - Sourced |
| false | true | false | Offer |
| false | true | true | Offer - Sourced |
| true | false | false | Action Group |
| true | false | true | Baseline |
| true | true | false | Offer Group |
| true | true | true | Baseline Offer |

------

This BigFix Session Relevance query determines the precise type of a BES Action. The logic is derived from the truth table above that evaluates all combinations of the following boolean properties:
- multiple flag of it
- offer flag of it
- exists source fixlet of it

```
(
  name of it,
  id of it,
  (
    if multiple flag of it then
      (
        if offer flag of it then
          (if exists source fixlet of it then "Baseline Offer" else "Offer Group")
        else
          (if exists source fixlet of it then "Baseline" else "Action Group")
      )
    else
      (
        if offer flag of it then
          (if exists source fixlet of it then "Offer - Sourced" else "Offer")
        else
          (if exists source fixlet of it then "Action - Sourced" else "Action")
      )
  ) of it
) of bes actions
```
