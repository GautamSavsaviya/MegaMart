
# MegaMart 

[![Build Status](https://img.shields.io/travis/GautamSavsaviya/MegaMart.svg?style=flat-square)](https://travis-ci.org/GautamSavsaviya/MegaMart)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Welcome to MegaMart, a powerful and user-friendly Django e-commerce website!

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Introduction

MegaMart is a feature-rich e-commerce website built using Django framework. It provides a seamless shopping experience for users and offers a wide range of products to choose from.

## Installation

To set up MegaMart locally, follow these steps:

  1. Clone the repository:
   ```
   
   git clone https://github.com/GautamSavsaviya/MegaMart.git
   ```
  2. Change into the project directory:
  ```

  cd MegaMart
  ```
  3. Create and activate a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate
  ```
  4. Install the required dependencies:
  ```
  pip install -r requirements.txt

  ```
  5. Apply the database migrations:
  ```
  python manage.py migrate

  ```
  6. Load sample data (optional):
  ```
  python manage.py loaddata fixtures/sample_data.json

  ```
  7. Start the development server:
  ```
  python manage.py runserver

  ```
  Access the website at http://localhost:8000 in your web browser.

## Configuration

Before running the project, make sure to configure the following settings:

Database: Update the DATABASES configuration in the settings.py file with your database credentials.
Environment Variables: Set up any necessary environment variables, such as API keys or secret keys, in a .env file.

## Usage

Here's how you can use MegaMart:

1. Visit the homepage to browse products, categories, and featured items.
2. Create an account or log in if you already have one.
3. Add products to your cart and proceed to checkout.
4. Provide shipping and payment information to complete the order.
5. Receive order confirmation and track the status of your orders in the user dashboard.
6. Enjoy the secure and user-friendly shopping experience provided by MegaMart.

### Documentation

For detailed documentation and API reference, please visit our wiki.

### Contributing

We welcome contributions from the community! To contribute to MegaMart, please follow these guidelines:

* Fork the repository and create a new branch for your feature or bug fix.
* Ensure that your code follows the project's coding standards and passes all tests.
* Submit a pull request with a clear description of your changes and their purpose.
* For more information, please refer to our contributing guidelines.

### License
This project is licensed under the MIT License.

### Contact Information
For any questions, feedback, or support requests, please feel free to contact us:

* Email: gautamsavsaviya17@gmail.com
* Twitter: @GautamSavsaviya
* GitHub: [GautamSavsaviya](https://github.com/GautamSavsaviya)
