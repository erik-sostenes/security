# HTTP Cookie

```
  |-------------------| ==========[ GET http://www.example.com/ HTTP/1.1 ]===========>|------------------|
	|       CLIENT      | <=========[ HTTP/1.1 200 OK SET-Cookie: sessionID ]==========>|       SERVER     |
	|-------------------| ==[ GET http://www.example.com/ HTTP/1.1 Cookie: sessionID ]=>|------------------|
```

**_Cookies are small text files that are stored on the user's device when browsing the web. These files contain information about the user's interactions on a specific website, such as language preferences, browsing preferences, log-in information, etc._**

### More information

[https://www.rfc-editor.org/rfc/rfc6265]

## Uses

**1.Remember login information**
**2.Personalization of the user experience**
**3.User tracking**
**4.Web analytics**
