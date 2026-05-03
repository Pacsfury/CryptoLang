import importlib

variables = {}
bindings = {}
used_add = []
modules = {}
code = []

def run_line(line):
    line = line.strip()
    if not line or line.startswith("//"): return

    if "->" in line:
        parts = line.split("->")
        var_name = parts[1].strip()
        user_input = input(parts[0].strip().replace('"', ''))
        variables[var_name] = int("".join(f"{ord(c):03d}" for c in user_input))

    elif "<-" in line:
        parts = line.split("<-")
        var_name = parts[0].strip()
        val_raw = parts[1].strip()
        if '"' in val_raw:
            clean_val = val_raw.replace('"', '')
            variables[var_name] = int("".join(f"{ord(c):03d}" for c in clean_val))
        else:
            variables[var_name] = int(val_raw)

    elif line.endswith(";"):
        variables[line.replace(";", "").strip()] = 0
    
    elif line.startswith("BASE "):
        variables["base"] = line[5:].strip()

    elif line.startswith("OUT "):
        parts = line[4:].split(" ")
        var_name = parts[0].strip()
        format_type = parts[1].strip()
        val = variables.get(var_name, 0)
        
        match format_type:
            case "BIN": print(f"{int(val):b}")
            case "INT": print(int(val))
            case "STR":
                if val is None: val = 0
                n = str(val)
                while len(n) % 3 != 0: n = "0" + n
                try:
                    print("".join([chr(int(n[i:i+3])) for i in range(0, len(n), 3)]))
                except:
                    print(f"[Error STR: {n}]")

    elif line.startswith("ADD "):
        mod_name = line[4:].strip()
        try:
            modules[mod_name] = importlib.import_module(f"add.{mod_name}")
            used_add.append(mod_name)
        except ImportError: pass

    else:
        if "." in line and "[" in line:
            parts = line.split(".", 1)
            mod_prefix = parts[0].strip()
            func_name = parts[1].split("[")[0].strip().replace(".", "")
            args_raw = parts[1].split("[")[1].replace("]", "").split(",")
            
            resolved_args = []
            for arg in args_raw:
                arg = arg.strip()
                if arg in variables:
                    resolved_args.append(variables[arg])
                else:
                    try:
                        resolved_args.append(int(arg))
                    except:
                        resolved_args.append(arg)

            if mod_prefix in modules:
                target = variables.get("base")
                if target:
                    res = modules[mod_prefix].run(func_name, resolved_args)
                    if res is not None:
                        variables[target] = res

    for key, target in bindings.items():
        if key in variables: variables[target] = variables[key]

while True:
    new_line = input()
    if new_line == "/RUN": break
    code.append(new_line)

for i in code:
    run_line(i)