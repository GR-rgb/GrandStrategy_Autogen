"""
custom_termination.py — Kondisi berhenti kustom: simulasi tamat kalau
2 dari 3 faksi sudah GUGUR atau MENYERAH (bukan langsung berhenti begitu
kata itu muncul sekali, seperti TextMentionTermination bawaan).

Catatan: API TerminationCondition bisa sedikit beda antar versi
autogen-agentchat. Kalau ada error saat import/pemakaian, cek signature
`TerminationCondition` di venv kamu:
    python -c "import inspect, autogen_agentchat.base as b; print(inspect.getsource(b.TerminationCondition))"
dan sesuaikan method __call__/reset di bawah kalau perlu.
"""

import re
from autogen_agentchat.base import TerminationCondition
from autogen_agentchat.messages import StopMessage


class FactionEliminationTermination(TerminationCondition):
    """Melacak faksi mana saja yang sudah dinyatakan GUGUR/MENYERAH oleh
    GameMaster (atau faksi itu sendiri), dan berhenti begitu jumlah faksi
    yang tersingkir mencapai `required_eliminations`."""

    def __init__(self, factions: list[str], required_eliminations: int = 2):
        self._factions = factions
        self._required = required_eliminations
        self._eliminated: set[str] = set()
        self._terminated = False

    @property
    def terminated(self) -> bool:
        return self._terminated

    async def __call__(self, messages):
        if self._terminated:
            return None

        for msg in messages:
            content = getattr(msg, "content", None)
            if not isinstance(content, str):
                continue
            for faction in self._factions:
                if faction in self._eliminated:
                    continue
                # cari "<NamaFaksi> ... GUGUR" atau "<NamaFaksi> ... MENYERAH"
                # dalam jarak dekat (maks ~60 karakter) di kalimat yang sama
                pattern = rf"{re.escape(faction)}[^\.\n]{{0,60}}(GUGUR|MENYERAH)"
                if re.search(pattern, content, re.IGNORECASE):
                    self._eliminated.add(faction)
                    print(f"[TERMINATION] Faksi tersingkir: {faction} "
                          f"({len(self._eliminated)}/{self._required})")

        if len(self._eliminated) >= self._required:
            self._terminated = True
            sisa = [f for f in self._factions if f not in self._eliminated]
            return StopMessage(
                content=(
                    f"Simulasi berakhir: {len(self._eliminated)} faksi "
                    f"tersingkir ({', '.join(sorted(self._eliminated))}). "
                    f"Faksi bertahan: {', '.join(sisa) if sisa else '-'}."
                ),
                source="FactionEliminationTermination",
            )
        return None

    async def reset(self) -> None:
        self._eliminated = set()
        self._terminated = False