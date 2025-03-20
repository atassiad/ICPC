def problem2():
    def most_used_app(screen_time):
        return max(screen_time, key = screen_time.get)
    screen_time = {"Instagram": 55, "YouTube": 30, "Snapchat": 15}
    screen_time_2 = {"Twitter": 25, "Reddit": 20, "Instagram": 35}
    screen_time_3 = {"TikTok": 90, "YouTube": 90, "Snapchat": 25}

    print(most_used_app(screen_time))
    print(most_used_app(screen_time_2))
    print(most_used_app(screen_time_3))

def problem3():
    def most_varied_app(app_usage):
        currentmax = 0
        return_app = ""
        for app, screentimes in app_usage.items():
            diff = max(screentimes) - min(screentimes)
            currentmax = max(currentmax, diff)
            if (currentmax == diff):
                return_app = app
        
        return return_app

    app_usage = {
        "Instagram": [60, 55, 65, 60, 70, 55, 60],
        "YouTube": [100, 120, 110, 100, 115, 105, 120],
        "Snapchat": [30, 35, 25, 30, 40, 35, 30]
    }

    app_usage_2 = {
        "Twitter": [15, 15, 15, 15, 15, 15, 15],
        "Reddit": [45, 50, 55, 50, 45, 50, 55],
        "Facebook": [80, 85, 80, 85, 80, 85, 80]
    }

    app_usage_3 = {
        "TikTok": [80, 100, 90, 85, 95, 105, 90],
        "Spotify": [40, 45, 50, 45, 40, 45, 50],
        "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
    }

    print(most_varied_app(app_usage))
    print(most_varied_app(app_usage_2))
    print(most_varied_app(app_usage_3))

#return max(app_usage, key=lambda x: max(app_usage[x]) - min(app_usage[x]))

def problem5():
    def find_longest_repeating_pattern(app_logs):
        freq_map = dict()
        current_list = []
        for app in app_logs:
            if (len(current_list) > 1 and current_list[0] == app):
                freq_map[tuple(current_list)] = freq_map.get((tuple(current_list)), 1) + 1
                current_list = []
            current_list.append(app)
        
        return max(freq_map, key = freq_map.get), max(freq_map.values())
                
    app_logs = ["Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Facebook", "Twitter", "Instagram"]
    app_logs_2 = ["Facebook", "Instagram", "Facebook", "Instagram", "Facebook", "Instagram", "Snapchat", "Snapchat", "Snapchat", "Instagram"]
    app_logs_3 = ["WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook", "WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook"]

    print(find_longest_repeating_pattern(app_logs))
    print(find_longest_repeating_pattern(app_logs_2))
    print(find_longest_repeating_pattern(app_logs_3))
problem5()