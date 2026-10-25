"""Verificação do custo das sessões do Claude Code: python3 test_custo_claude.py"""
import json
import tempfile
from pathlib import Path

import server

# 1M de cada, Opus 5.5: 4 + 20 + 0,20 + 8 (escrita de 1 h) = 32,20 $
u = {"input_tokens": 1_000_000, "output_tokens": 1_000_000, "cache_read_input_tokens": 1_000_000,
     "cache_creation_input_tokens": 1_000_000,
     "cache_creation": {"ephemeral_1h_input_tokens": 1_000_000, "ephemeral_5m_input_tokens": 0}}
assert abs(server.custo_usage("claude-opus-5-5", u) - 32.20) < 1e-9
assert abs(server.custo_usage("claude-opus-5", u) - (5 + 25 + 0.5 + 10)) < 1e-9   # o prefixo mais comprido ganha
assert server.custo_usage("gpt-qualquer", u) is None

with tempfile.TemporaryDirectory() as d:
    sid = "00000000-0000-4000-8000-000000000001"
    proj = Path(d) / "-proj"
    (proj / sid / "subagents").mkdir(parents=True)
    msg = lambda i, m="claude-opus-5-5": json.dumps({"type": "assistant", "message": {
        "id": i, "model": m, "usage": {"input_tokens": 0, "output_tokens": 1_000_000}}})
    # a mesma mensagem em duas linhas conta uma vez; o sub-agente soma
    (proj / f"{sid}.jsonl").write_text("\n".join([msg("a"), msg("a"), msg("b", "modelo-novo")]))
    (proj / sid / "subagents" / "agent-x.jsonl").write_text(msg("c"))
    server.CLAUDE_PROJECTS = Path(d)
    st, r = server.custo_claude(sid)
    assert st == 200 and abs(r["usd"] - 40) < 1e-9 and r["sem_preco"] == ["modelo-novo"], r
    assert server.custo_claude("../../etc/passwd")[0] == 400
print("ok")
