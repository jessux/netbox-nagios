import json
import requests

def hoststatus(hostname: str, livestatus_host: str, livestatus_port: int):
    # """Fetches livestatus from Nagios about hostname."""
    # query = (
    #     "GET hosts\n"
    #     + "Filter: host_name = %s\n" % hostname  #
    #     + "OutputFormat: json\n"
    # )

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(TIMEOUT)
    # s.connect((livestatus_host, livestatus_port))
    # s.sendall(query.encode("utf-8"))
    # s.shutdown(socket.SHUT_WR)

    # data = []
    # while True:
    #     buf_data = s.recv(BUFFER_SIZE)
    #     if not buf_data:
    #         break
    #     data.append(buf_data)
    # s.close()
    payload = {'username': 'admin','password': 'centreon'}
    response = requests.request("POST", "http://digsflrp1k.dig.intra.groupama.fr/centreon/api/index.php?action=authenticate", data=payload)
    if response.status_code == 200:
        url = "http://digsflrp1k.dig.intra.groupama.fr/centreon/api/index.php?object=centreon_realtime_hosts&action=list&search="+hostname
        payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\"\r\n}"
        headers = {
            'Content-Type': 'application/json',
            'centreon-auth-token': response.json()["authToken"],
            'Content-Type': 'text/plain'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        j = json.loads(response.text.encode('utf-8'))[0]
        print(j)
        result = dict(zip("state",j.state))
        print(result)
        return result

