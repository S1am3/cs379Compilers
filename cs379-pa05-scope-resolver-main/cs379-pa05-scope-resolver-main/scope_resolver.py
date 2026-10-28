"""
PA 5: The Scope Resolver -- starter.

Complete resolve_name below. See the assignment, Part B,
for the full requirements.
"""

from typing import List

from symtable import Environment, SemanticError


def resolve_name(
    name: str,
    current_env: Environment,
    call_stack: List[Environment],
    mode: str,
) -> int:
    """
    Return the declaration line `name` resolves to.

    mode == "static": climb current_env.parent links (ignore call_stack).
    mode == "dynamic": search call_stack from most-recent (index -1)
        to oldest (index 0), checking each caller's OWN locally-defined
        names only (not their parents), falling back to the global
        (outermost lexical) environment if not found on the stack.
    Any other mode raises ValueError. Raise SemanticError if `name`
    cannot be resolved under the requested mode.
    """
    # TODO
    # if mode is not static and not dynamic raise error
    if mode != "static" and mode != "dynamic":
        raise ValueError("Has to be Static or Dynamic!")
    

    if mode == "static":
        return current_env.resolve(name)

    for env in reversed(call_stack):
        if name in env._names:
            return env._names[name]

    globalEnv = current_env
    while globalEnv.parent is not None:
        globalEnv = globalEnv.parent

    if name in globalEnv._names:
        return globalEnv._names[name]

    raise SemanticError(f"undefined var, {name}")
