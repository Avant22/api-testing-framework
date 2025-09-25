# 📝 Manual Test Plan

## Test Scenarios

### 1. Get Users - Positive
**Steps:**
1. Call `GET /users`
2. Verify status = 200
3. Verify response is a JSON list
4. Verify each user has `id, name, username, email`

**Expected Result:**  
Valid list of users returned.

---

### 2. Get User - Negative
**Steps:**
1. Call `GET /users/9999`
2. Verify status = 404
3. Verify error message returned

**Expected Result:**  
`404 Not Found` with JSON error.

---

### 3. Performance Baseline
**Steps:**
1. Call `GET /users` 1000 times under load
2. Measure average response time

**Expected Result:**  
Average < 500ms, error rate < 1%.
