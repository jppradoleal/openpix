# Open Pix SDK for Python

Library made to provide developers with bindings to help you integrate OpenPix API to your system and start receiving pix payments.

> This lib is deeply based in Mercado Pago SDK.

## Getting Started

1. Create your [OpenPix account](https://openpix.com.br/register/?src=header).
2. Go to `Config > Pix > Go to Advanced Options`, 
   1. Create a testing bank account
   2. Set it as default while you're testing your API.
3. Go to API/Plugins.
4. Create a new API.
   1. Give it a name.
   2. Select API Rest.
   3. Choose the bank account.
5. Access your newly created API.
6. Copy the App ID.

### Simple usage

```python
import openpix
from openpix.core.entities import ChargeObject

sdk = openpix.SDK("YOUR_APP_ID")

charge_data = ChargeObject(value=1000, correlationID="1")
result = sdk.charge().create(charge)
charge = result["response"]

print(charge)
```

## Documentation

Visit [Open Pix Docs](https://developers.openpix.com.br/docs/apis/api-getting-started/) for further information about the API.

We're following the [Postman](https://developers.openpix.com.br/openpixPostman.json) listed routes.

## Contributing

All contributions are welcome, ranging from people wanting to triage issues, others wanting to write documentation, to people wanting to contribute code.

Please read and follow our [contribution guidelines](CONTRIBUTING.md). Contributions not following this guidelines will be disregarded. The guidelines are in place to make all of our lives easier and make contribution a consistent process for everyone.

## License

MIT license. Copyright (c) 2022 - João Prado.

For more information, see the [LICENSE](LICENSE.md) file.