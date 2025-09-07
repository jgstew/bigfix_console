# bigfix_console
A BigFix console console. A BigFix interactive console program written in Python using Textual.


## BigFix Action Type Logic Truth Table
This table maps the possible boolean combinations of BigFix Action properties to a specific Action Type.

| multiple flag | offer flag | exists source fixlet | Resulting Action Type |
| false | false | false | Action |
| false | false | true | Action - Sourced |
| false | true | false | Offer |
| false | true | true | Offer - Sourced |
| true | false | false | Action Group |
| true | false | true | Baseline |
| true | true | false | Offer Group |
| true | true | true | Baseline Offer |
