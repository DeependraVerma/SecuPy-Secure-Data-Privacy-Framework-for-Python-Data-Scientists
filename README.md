# SheildPy: Secure Data Privacy Framework for Python Data Scientists

[![GitHub stars](https://img.shields.io/github/stars/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists.svg)](https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists/stargazers)
[![GitHub license](https://img.shields.io/github/license/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists.svg)](https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists/blob/main/LICENSE)

SheildPy is an all-in-one Python package designed to address data privacy and security concerns for data scientists. Developed by [Deependra Verma](https://www.linkedin.com/in/deependra-verma-data-science/), SheildPy offers robust encryption, anonymization, and access control tools, ensuring the confidentiality and integrity of sensitive data.

## Introduction

SheildPy: Your all-in-one Python package for robust data privacy and security. Encrypt, anonymize, and control access to sensitive data effortlessly.

## Features

### SheildPy provides the following key methods:
- `encrypt_data(data)`: Encrypts sensitive data to ensure confidentiality.
- `decrypt_data(encrypted_data)`: Decrypts encrypted data to its original form.
- `anonymize_data(data, columns_to_anonymize)`: Anonymizes specific columns in a DataFrame.
- `add_role(role_name, permissions)`: Adds a new role with associated permissions to the access control system.
- `check_permission(role_name, permission)`: Checks if a role has the specified permission.

## Installation

To install SheildPy, simply run:

```bash
pip install SheildPy
```

Alternatively, you can clone the GitHub repository:

```bash
git clone https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists.git
cd SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists
python setup.py install
```

## Dependencies

SheildPy relies on the following dependencies:
- `pandas>=1.0.0`
- `faker>=8.0.0`
- `cryptography>=3.0`

## Usage


# Import the package
from PrivacyPy import DataPrivacyFramework

# Initialize PrivacyPy with encryption key
encryption_key = "your_encryption_key"
privacy_framework = DataPrivacyFramework(encryption_key)

# Anonymize sensitive columns (Name, Email)
anonymized_df = privacy_framework.anonymize_data(data, ['Name', 'Email'])

# Encrypt entire DataFrame
encrypted_df = privacy_framework.encrypt_data(anonymized_df)
print("Encrypted DataFrame:")
print(encrypted_df)


## Users Benefit

SheildPy empowers data scientists with the following benefits:
- **Data Confidentiality:** Encrypt sensitive data to prevent unauthorized access.
- **Anonymization:** Anonymize personally identifiable information for privacy protection.
- **Access Control:** Control data access based on user roles and permissions.
- **Compliance:** Ensure compliance with data protection regulations (e.g., GDPR, HIPAA).

## Use Cases

SheildPy can be used in various data science scenarios, including:
- Healthcare data analysis
- Financial data processing
- User authentication systems
- Research collaborations with external parties


## Invitation for Contribution

Contributions to SheildPy are welcome! To contribute, follow these steps:
1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your modifications and improvements.
5. Test your changes to ensure they work as expected.
6. Commit your changes and push them to your forked repository.
7. Submit a pull request to the original repository.

We welcome contributions from the community! Whether it's fixing bugs, adding new features, or improving documentation, your contributions help make XplainML better for everyone. Check out our [Contributing Guidelines](https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists/wiki) to get started.

## License

SheildPy is licensed under the [MIT License](https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists/blob/main/LICENSE). See the [LICENSE](https://github.com/DeependraVerma/SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists/blob/main/LICENSE) file for details.

## About the Author

[Email](mailto:deependra.verma00@gmail.com) | [LinkedIn](https://www.linkedin.com/in/deependra-verma-data-science/) | [GitHub](https://github.com/DeependraVerma) | [Portfolio](https://deependradatascience-productportfolio.netlify.app/)
