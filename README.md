# Localbitcoins API client

This is a very simple example of a client for Localbitcoins API. All calls are yet to be supported, but you can get the idea on how to use the API for your own needs. The client is run from command line, and the servers' response is printed to the standard output in user friendly JSON-format.

The client is tested to work with Python2.7 and requires ```requests``` library.

## How to install
1. Go to https://localbitcoins.com/accounts/api and add an HMAC key to your account. Remember to keep it safe!
2. Update the file settings.py with your HMAC key & secret
3. Test the client: ```python lbc-client.py myself```

## Supported calls (See: https://localbitcoins.com/api-docs/)

| API                      | Client command     | Method | Access tokens | Required arguments | Optional arguments |
|--------------------------|--------------------|--------|---------------|--------------------|--------------------|
| /api/account_info/       | account_info       | GET    | Public        | username           |                    |
| /api/myself/             | myself             | GET    | read          |                    |                    |
| /api/dashboard/          | dashboard          | GET    | read          |                    |                    |
| /api/dashboard/released/ | dashboard/released | GET    | read          |                    |                    |
| /api/dashboard/canceled/ | dashboard/canceled | GET    | read          |                    |                    |
| /api/dashboard/closed/   | dashboard/closed   | GET    | read          |                    |                    |
| /api/contact_messages/   | contact_messages   | GET    | read          | contact_id         |                    |
| /api/contact_info/       | contact_info       | GET    | read          | contact_ids as csv |                    |
| /api/recent_messages/    | recent_messages    | GET    | read          |                    | before             |
| /api/wallet/             | wallet             | GET    | read          |                    |                    |
| /api/wallet-send/        | wallet-send        | POST   | money         | address, amount    |                    |
| /api/wallet-balance/     | wallet-balance     | GET    | read          |                    |                    |