import subprocess as sub

data = (
    sub.check_output(["netsh", "wlan", "show", "profile"])
    .decode("utf-8")
    .split("\n")
)

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = (
            sub.check_output(["netsh", "wlan", "show", "profiles",i,"key=clear"])
            .decode("utf-8")
            .split("\n")
        )
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, "No"))
