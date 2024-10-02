# Modul Pengguna - untuk menambahkan dan mendaftarkan pengguna
class UserModule:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        self.users.append(username)
        print(f"User {username} ditambahkan")

    def display_users(self):
        print("Daftar pengguna yang terdaftar:")
        for user in self.users:
            print(f"- {user}")

# Modul Dashboard - statistik penggunaan alat
class DashboardModule:
    def __init__(self):
        self.stats = {}

    def update_stats(self, tool_name, usage_count):
        self.stats[tool_name] = usage_count

    def display_stats(self):
        print("Statistik Penggunaan:")
        for tool, count in self.stats.items():
            print(f"{tool}: {count} kali digunakan")

# Modul Log Activity - mencatat aktivitas pengguna
class LogActivityModule:
    def __init__(self):
        self.logs = []

    def log_activity(self, user, activity):
        log = f"{user} melakukan {activity}"
        self.logs.append(log)
        print(log)

    def display_logs(self):
        print("Log Aktivitas:")
        for log in self.logs:
            print(log)

# Modul Master - CRUD data master
class MasterModule:
    def __init__(self):
        self.data_master = []

    def create_master_data(self, data):
        self.data_master.append(data)
        print(f"Data master '{data}' ditambahkan")

    def read_master_data(self):
        print("Data Master:")
        for data in self.data_master:
            print(f"- {data}")

    def update_master_data(self, index, new_data):
        if 0 <= index < len(self.data_master):
            old_data = self.data_master[index]
            self.data_master[index] = new_data
            print(f"Data master '{old_data}' diubah menjadi '{new_data}'")
        else:
            print("Index tidak valid")

    def delete_master_data(self, index):
        if 0 <= index < len(self.data_master):
            removed_data = self.data_master.pop(index)
            print(f"Data master '{removed_data}' dihapus")
        else:
            print("Index tidak valid")

# Contoh penggunaan dari modul-modul di atas
if __name__ == "__main__":
    # Menggunakan Modul Pengguna
    user_module = UserModule()
    user_module.add_user("Alice")
    user_module.add_user("Bob")
    user_module.display_users()

    # Menggunakan Modul Dashboard
    dashboard_module = DashboardModule()
    dashboard_module.update_stats("Tool A", 5)
    dashboard_module.update_stats("Tool B", 3)
    dashboard_module.display_stats()

    # Menggunakan Modul Log Activity
    log_module = LogActivityModule()
    log_module.log_activity("Alice", "Menggunakan Tool A")
    log_module.log_activity("Bob", "Menggunakan Tool B")
    log_module.display_logs()

    # Menggunakan Modul Master
    master_module = MasterModule()
    master_module.create_master_data("Data 1")
    master_module.create_master_data("Data 2")
    master_module.read_master_data()
    master_module.update_master_data(0, "Data 1 Updated")
    master_module.read_master_data()
    master_module.delete_master_data(1)
    master_module.read_master_data()
