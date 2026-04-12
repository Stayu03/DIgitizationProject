#!/usr/bin/env python3
from webapp import app

c = app.test_client()
# Login first
c.post('/login', data={'email':'admindigisys1_cu@gmail.com','password':'adad1234'}, follow_redirects=True)

# Test 1: Check user management page
resp = c.get('/user-management')
html = resp.get_data(as_text=True)

if 'mini-btn reset' in html:
    print('✗ Reset password button still exists in user management')
else:
    print('✓ Reset password button removed from user management')

# Test 2: Check if user table has border-spacing
if 'border-spacing: 0 8px' in html:
    print('✓ User table has border-spacing: 0 8px')
else:
    print('✗ User table border-spacing not found')

# Test 3: Check if border-radius is applied
if 'border-radius: 8px' in html:
    print('✓ Border-radius: 8px applied')
else:
    print('✗ Border-radius: 8px not found')

# Test 4: Check documents page for pattern-table styling
resp2 = c.get('/documents')
html2 = resp2.get_data(as_text=True)

if 'border-spacing: 0 8px' in html2:
    print('✓ Pattern table has border-spacing: 0 8px (documents page)')
else:
    print('✗ Pattern table border-spacing not found')

# Test 5: Check for breadcrumb script
if 'page_breadcrumb' in html or 'page_breadcrumb' in html2:
    print('✓ Breadcrumb tracking script found')
else:
    print('✗ Breadcrumb tracking script not found')

print("\nAll tests completed!")
