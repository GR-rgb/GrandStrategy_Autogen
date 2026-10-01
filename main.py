import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from personas import GM_PROMPT, WEI_PROMPT, CHAOS_PROMPT, BALANCER_PROMPT
from map_data import MAP_DESCRIPTION
from custom_termination import FactionEliminationTermination

model_info = {
    "vision": False,
    "function_calling": True,
    "json_output": False,
    "family": "unknown",
    "structured_output": False,
}

def make_client():
    return OpenAIChatCompletionClient(
        model="qwen2.5:7b-instruct",
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model_info=model_info,
        temperature=0.3,  # diturunkan dari default supaya output lebih stabil, kurang "ngaco"
    )

gm = AssistantAgent(name="GameMaster", model_client=make_client(), system_message=GM_PROMPT + "\n\n" + MAP_DESCRIPTION)
wei = AssistantAgent(name="Wei_Utara", model_client=make_client(), system_message=WEI_PROMPT + "\n\n" + MAP_DESCRIPTION)
chaos = AssistantAgent(name="Wildcard_Tengah", model_client=make_client(), system_message=CHAOS_PROMPT + "\n\n" + MAP_DESCRIPTION)
balancer = AssistantAgent(name="Selatan", model_client=make_client(), system_message=BALANCER_PROMPT + "\n\n" + MAP_DESCRIPTION)

# Daftar faksi yang dipantau untuk kondisi berhenti
FACTIONS = ["Wei_Utara", "Wildcard_Tengah", "Selatan"]

# Kondisi berhenti: tamat kalau 2 dari 3 faksi sudah GUGUR/MENYERAH,
# ATAU sudah 40 pesan (safety net kalau perang berlarut-larut tanpa ada yang jatuh)
termination = FactionEliminationTermination(FACTIONS, required_eliminations=2) | MaxMessageTermination(40)

team = RoundRobinGroupChat(
    participants=[gm, wei, chaos, balancer],
    termination_condition=termination,
)

SKENARIO_AWAL = """Simulasi dimulai di dunia Aldoria.

KONDISI AWAL:
- Wei_Utara menguasai kota Utara: Pasukan Besar, Pangan Cukup, Uang Kaya.
- Wildcard_Tengah menguasai kota Tengah: Pasukan Kecil, Pangan Menipis, Uang Cukup (kecil tapi berbahaya, netral terhadap semua).
- Selatan menguasai kota Selatan: Pasukan Sedang, Pangan Cukup, Uang Cukup.

GameMaster, silakan buka ronde pertama dengan mengumumkan kondisi awal ini via format [STATE] untuk SEMUA TIGA faksi, HANYA pakai kategori label (jangan angka). ATURAN KHUSUS RONDE PERTAMA: Wildcard_Tengah WAJIB melakukan aksi menyerang ke salah satu tetangganya (Wei_Utara atau Selatan) di giliran pertamanya. Setelah itu faksi bebas menentukan aksi TEGAS setiap giliran (menyerang, bertahan aktif, diplomasi, atau beli pangan) — dilarang keras hanya "menunggu" tanpa aksi nyata."""

async def main():
    await Console(team.run_stream(task=SKENARIO_AWAL))

asyncio.run(main())