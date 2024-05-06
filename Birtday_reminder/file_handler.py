class FileHandler:
    @staticmethod
    def read_from_file(filename):
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
            return data
        except FileNotFoundError:
            print("File not found.")
            return []

    @staticmethod
    def write_to_file(data, filename):
        try:
            with open(filename, 'w') as file:
                for item in data:
                    file.write(item + '\n')
            print("Data written to file successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")