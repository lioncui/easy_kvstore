#easy_kvstore

##summary
This is an easy key/value store server.

1. Start Server
    ```bash
    python kvserver.py
    2016-03-30 15:46:29 Starting kvserver now....
    ```

2. Connect Server
    ```bash
    python kvclient.py
    localhost:6375> 
    localhost:6375> help
    help                - print help_doc .
    set <key> <value>   - store the key/value .
    get <key>           - get the vaule of <key> .
    flushall            - clean the store data . 
    exit                - exit connection .
    localhost:6375> exit
    ```
