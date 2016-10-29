# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010, 2014 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Simplyrets_1_0_0 Integration',
    'version': '0.1',
    'author': 'Cenit IO',
    'website': 'https://cenit.io',
    # ~ 'license': 'LGPL-3',
    'category': 'Extra Tools',
    'summary': 'The SimplyRETS API is an exciting step towards making it easier for
developers and real estate agents to build something awesome with
real estate data!

The documentation below makes live requests to our API using the
trial data. To get set up with the API using live MLS data, you
must have RETS credentials from your MLS, which you can then use to
create an app with SimplyRETS. For more information on that
process, please see our [FAQ](https://simplyrets.com/faq), [Getting
Started](https://simplyrets.com/blog/getting-set-up.html) page, or
[contact us](https://simplyrets.com/\#home-contact).

Below you'll find the API endpoints, query parameters, response bodies,
and other information about using the SimplyRETS API. You can run
queries by clicking the 'Try it Out' button at the bottom of each
section.

### Authentication
The SimplyRETS API uses Basic Authentication. When you create an
app, you'll get a set of API credentials to access your
listings. If you're trying out the test data, you can use
`simplyrets:simplyrets` for connecting to the API.

### Media Types
The SimplyRETS API uses the `Accept` header to allow clients to
control media types (content versions). We maintain backwards
compatibility with API clients by allowing them to specify a
content version. We highly recommend setting and explicity media
type when your application reaches production. Both the structure
and content of our API response bodies is subject to change so we
can add new features while respecting the stability of applications
which have already been developed.

To always use the latest SimplyRETS content version, simply use
`application/json` in your application `Accept` header.

If you want to pin your clients media type to a specific version,
you can use the vendor-specific SimplyRETS media type, e.g.
`application/vnd.simplyrets-v0.1+json"`

To view all valid content-types for making an `OPTIONS`, make a
request to the SimplyRETS api root

`curl -XOPTIONS -u simplyrets:simplyrets https://api.simplyrets.com/`

The default media types used in our API responses may change in the
future. If you're building an application and care about the
stability of the API, be sure to request a specific media type in the
Accept header as shown in the examples below.

The wordpress plugin automatically sets the `Accept` header for the
compatible SimplyRETS media types.

### Pagination
There a few pieces of useful information about each request stored
in the HTTP Headers:

- `X-Total-Count` shows you the total amount of listings that match
  your current query.
- `Link` contains pre-built pagination links for accessing the next
'page' of listings that match your query. Read more about that
[here](https://simplyrets.com/blog/api-pagination.html).
',
    'description': """
        Odoo - Simplyrets_1_0_0 integration via Cenit IO
    """,
    'depends': ['cenit_base'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True
}
