# aiida-donothing

AiiDA calculation plugin for doing nothing. This is used as a wrapper of `sleep`
command.

### Example

```bash
% verdi code show donothing@localhost
--------------------  ------------------------------------
PK                    147942
UUID                  123e4567-e89b-12d3-a456-426614174000
Label                 donothing
Description
Default plugin        donothing.donothing
Type                  remote
Remote machine        localhost
Remote absolute path  /bin/sleep
Prepend text
Append text
--------------------  ------------------------------------
```

```python
In [1]: code = Code.get_from_string('donothing@localhost')

In [2]: builder = code.get_builder()

In [3]: builder.metadata.options.resources = {"parallel_env": "default", "tot_num_mpiprocs": 1}

In [4]: builder.seconds = Int(60)

In [5]: from aiida.engine import run

In [6]: run(builder)
```
