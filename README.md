
IRKit Client
==============

Usage:
--------------

```python
#!/usr/bin/env python

from irkit import IRKitInternetAPI

clientkey = '<YOUR_CLIENT_KEY>'
deviceid = '<YOUR_DEVICE_ID>'

irkit = IRKitInternetAPI(clientkey, deviceid)

data = [18031, 8755, 1190, 1037, 1190, 1037]
irkit.post_messages(data)
```

