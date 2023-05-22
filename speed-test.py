import os
try:
    import speedtest
except:
    os.system('pip install speedtest-cli')
    import speedtest
    
test = speedtest.Speedtest()

# test.get_servers()
# best = test.get_best_server()

down_speed = test.download()
up_speed = test.upload()

print('please wait ...')

print(f"""
download: {down_speed / 1024 / 1024:.2f} Mb-it/s
upload: {up_speed / 1024 / 1024:.2f} Mb-it/s
""")