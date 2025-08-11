# Useful Packages

- **argparse** – standard library for CLI applications
- **typer** – helps develop CLI applications
- **tenacity**
- **retry**
- **rich** – rich text formatting in the terminal; better traceback, progress bar, etc.
- **glom**
- **loguru**
- **sparkles.sorted_groupby**
- **pytest**
- **pytest‑watch**
- **pyfakerfs**
- **ptvsd**

- **yt‑dlp** – video downloader

```bash
python -m ptvsd flask run -wait
```

```json
{
    "name": "Python Debugger",
    "type": "python",
    "request": "attach",
    "pathMappings": [
        {
            "localRoot": "C:\\user\\twu\\xxx",
            "remoteRoot": "/app"
        }
    ],
    "port": 1000,
    "host": "localhost"
}
```

## Interesting Pattern

<https://github.com/python-gitlab/python-gitlab/blob/336ee21779a55a1371c94e0cd2af0b047b457a7d/gitlab/client.py#L34>
