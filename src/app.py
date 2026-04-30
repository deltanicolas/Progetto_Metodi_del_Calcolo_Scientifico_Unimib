#!/usr/bin/env python3
from pathlib import Path
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Input, Label, OptionList, RichLog
from textual.widgets.option_list import Option
from test import run_specific_test 



SOLVERS = ["jacobi", "gs", "grad", "cg"]
DATA_DIRS = [Path("../Data"), Path("./Data"), Path("../../Data")]

class ProgettoMCSApp(App):
    TITLE = "MCS Dashboard — Iterative Solvers"
    BINDINGS = [
        Binding("ctrl+r", "run", "Run Solver", show=True),
        Binding("ctrl+c", "clear", "Clear Output", show=True),
        Binding("ctrl+q", "quit", "Exit", show=True),
    ]

    CSS = """
    Screen { background: #1a1b26; color: #a9b1d6; }
    Header, Footer { background: #24283b; color: #7aa2f7; }
    #sidebar { width: 35%; border-right: tall #414868; padding: 1; }
    OptionList { background: #24283b; border: solid #414868; height: 7; margin: 1 0; }
    #console { background: #16161e; border: double #7aa2f7; padding: 1; height: 1fr; }
    Input { background: #24283b; border: solid #414868; color: #2ac3de; }
    #main-content { width: 65%; padding: 1; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Label("📁 MATRICI (.mtx)", classes="section-title")
                yield OptionList(id="file_list")
                
                yield Label("⚙️  METODO", classes="section-title")
                yield OptionList(Option("All Methods", id="all"), 
                                 *[Option(m.upper(), id=m) for m in SOLVERS], id="method_list")
                
                yield Label("🎯 TOLLERANZA", classes="section-title")
                yield Input(value="1e-6", id="input_tol")
            with Vertical(id="main-content"):
                yield RichLog(id="console", highlight=True, markup=True)
        yield Footer()

    def on_mount(self) -> None:
        self._log("[bold cyan]MCS Dashboard Pronta!\n seleziona un file, un metodo e una tolleranza per iniziare[/]\n [italic yellow]ctrl+r: esegui | ctrl+c: pulisci console | ctrl+q: esci [/]")
        data_dir = next((p for p in DATA_DIRS if p.is_dir()), None)
        flist = self.query_one("#file_list", OptionList)
        
        if data_dir and (files := sorted(data_dir.glob("*.mtx"))):
            for f in files: flist.add_option(Option(f.name, id=str(f)))
        else:
            flist.add_option(Option("❌ Nessun file .mtx trovato", id="none"))
        
        self.query_one("#method_list", OptionList).highlighted = 0

    def _log(self, msg: str, style: str = "") -> None:
        self.query_one("#console", RichLog).write(f"[{style}]{msg}[/]" if style else msg)

    def action_clear(self) -> None:
        self.query_one("#console", RichLog).clear()
        self._log(">>> [bold cyan]Console pulita[/]")

    def action_quit(self) -> None:
        self.exit()

    def action_run(self) -> None:
        flist, mlist = self.query_one("#file_list", OptionList), self.query_one("#method_list", OptionList)
        if flist.highlighted is None or mlist.highlighted is None: return
        
        file_id = flist.get_option_at_index(flist.highlighted).id
        method_id = mlist.get_option_at_index(mlist.highlighted).id
        if file_id == "none": return self._log("❌ Nessun file valido selezionato", "bold red")

        try:
            tol = float(self.query_one("#input_tol", Input).value)
        except ValueError:
            return self._log("❌ Tolleranza non valida", "bold red")

        methods_to_run = SOLVERS if method_id == "all" else [method_id]
        
        self._log(f"\n🚀 [bold white]ESECUZIONE: {Path(file_id).name} | Tol: {tol:.0e}[/]") # type: ignore
        self._log("METODO     | STATUS   | ITERAZIONI | TEMPO (s) | ERRORE", "bold cyan")
        self._log("-----------+----------+------------+-----------+----------", "cyan")

        for m in methods_to_run:
            try:
                res = run_specific_test(file_id, m, tol) # type: ignore
                ok, it = res.get("converged", False), int(res.get("iterations", 0))
                t_s, err = float(res.get("time", 0.0)), float(res.get("error", 0.0))
                status = "[green]✅ OK  [/]" if ok else "[red]❌ FAIL[/]"
                self._log(f"{m.upper():<10} | {status} | {it:>10} | {t_s:>9.5f} | {err:.2e}") # type: ignore
            except Exception as e:
                self._log(f"{m.upper():<10} | [red]❌ ERR [/] | Errore: {e}") # type: ignore

if __name__ == "__main__":
    ProgettoMCSApp().run()