# Prefect FH Kufstein Demo

## Authors

- Aichinger-Fankhauser Peter
- Beyerle Gregor
- Reckmeyer Elias
- Ustaszewski Michael

## Content

This repository includes a demo [Prefect](https://docs.prefect.io/) flow that collects information about
air crafts in a radius around an airport (Vienna International Airport in our case) and saves them in a
SQLite database. The example was taken from the
[official ETL guide](https://docs.prefect.io/core/tutorial/01-etl-before-prefect.html).

The flow assumes that it won't be directly run but registered on a backend. If you don't have a Prefect
Cloud account you can create a local backend using docker. Make sure that you have docker and docker-compse
installed.

To specify the local backend execute

```bash
prefect backend server
```

If you don't have the server running already you can start it with the following command.
This will take a while for the first startup as the system will download a couple of images.

```bash
prefect server start
```

The flow assumes that a project called `aircraft-etl` exists on the server. You can create it with
the following command

```bash
prefect create project "aircraft-etl"
```

Now you can register the flow by running the script. If you want to update the flow you should be
able to add your changes and then rerun the script (given that you didn't change the flow name).

```bash
python ./aircraft_etl_flow.py
```

The server (or the cloud for that matter as far as we are aware of) doesn't run your tasks without
providing agents. Run a local agent which receives commands from the server like this

```bash
prefect agent local start
```

Be aware that if you have a scheduled flow (like we have here) and there is a long time between registering
the flow and starting the agent there might be a queue of flow executions waiting. With SQLite being
a file based data base this might lead to task failures.

## Complementary Tutorial

This tutorial is complemented by an [additional tutorial](https://colab.research.google.com/drive/1g4H0oY4Sbk8KhdXIFYAN_kUc4g4RDwVT#scrollTo=M_mzEt4RhAYO), which demonstrates a minimal ETL workflow for RSS feed data implemented in Prefect.