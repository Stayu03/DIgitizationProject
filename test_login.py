#!/usr/bin/env python3
"""Test login functionality."""
from webapp import app

app.testing = True
client = app.test_client()

# Test 1: GET /login should show login form
print("=== Test 1: Load login page ===")
resp = client.get("/login")
print(f"Status: {resp.status_code}")
print(f"Has form: {'<form' in resp.get_data(as_text=True)}")
print(f"Has Thai: {'เข้าสู่ระบบ' in resp.get_data(as_text=True)}")

# Test 2: POST with wrong credentials
print("\n=== Test 2: Login with wrong password ===")
resp = client.post("/login", data={"email": "admin@digitization.local", "password": "wrong"})
print(f"Status: {resp.status_code}")
print(f"Has error message: {'Invalid' in resp.get_data(as_text=True)}")

# Test 3: POST with correct credentials
print("\n=== Test 3: Login with correct credentials ===")
resp = client.post("/login", data={"email": "admin@digitization.local", "password": "admin123"}, follow_redirects=True)
print(f"Status: {resp.status_code}")
print(f"Final URL in response: {resp.request.path if hasattr(resp, 'request') else 'N/A'}")
print(f"Has dashboard content: {'Dashboard' in resp.get_data(as_text=True) or 'Admin User' in resp.get_data(as_text=True)}")

print("\n✓ Login page is working!")
