import pandas as pd
from cryptography.fernet import Fernet
import uuid
import os

class DataPrivacyFramework:
    def __init__(self, encryption_key):
        self.fernet = Fernet(encryption_key)
        self.anonymized_columns = set()
        self.identifier = str(uuid.uuid4())

    def anonymize_data(self, df, columns_to_anonymize):
        anonymized_df = df.copy()
        anonymized_df['_identifier'] = self.identifier
        for column in columns_to_anonymize:
            anonymized_df[column] = anonymized_df[column].apply(lambda x: '*****' if pd.notnull(x) else x)
            self.anonymized_columns.add(column)
        return anonymized_df

    def encrypt_data(self, data):
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.fernet.decrypt(encrypted_data).decode()
        return decrypted_data

    def decrypt_column(self, encrypted_column):
        decrypted_column = encrypted_column.apply(self.decrypt_data)
        return decrypted_column

    def encrypt_confidential_data(self, df, confidential_columns):
        encrypted_df = df.copy()
        for column in confidential_columns:
            encrypted_df[column] = df[column].apply(lambda x: self.encrypt_data(str(x)) if pd.notnull(x) else x)
        return encrypted_df

    def decrypt_dataframe(self, df):
        decrypted_df = df.copy()
        for column in df.columns:
            decrypted_df[column] = self.decrypt_column(df[column])
        return decrypted_df

def generate_encryption_key():
    return Fernet.generate_key()

def load_encryption_key(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return f.read()
    else:
        return None

def save_encryption_key(encryption_key, file_path):
    with open(file_path, 'wb') as f:
        f.write(encryption_key)
