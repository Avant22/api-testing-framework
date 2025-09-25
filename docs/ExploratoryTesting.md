# 🔍 Exploratory Testing Approach

## Charter
- Explore edge cases around `users` endpoint.
- Validate error handling and unusual inputs.
- Investigate undocumented behaviors.

## Example Tests
- Call `/users?page=-1`
- Call `/users?page=abc`
- Call `/users` with very high page number
- Modify headers (invalid auth token, missing headers)

## Recording
- Issues logged in Jira with reproduction steps.
- Insights used to design new automated test cases.
