from rich.table import Table

def render_tab(console,input):
    table = Table(show_header=True, header_style="bold magenta")
    
    # Add headers to the table
    for header in input[0].keys():
        table.add_column(header)
    
    # Add rows to the table
    
    for row in input:
        state = row["STATE"]
        # Apply green for "Available" and red for "Shutdown"
        state_style = "[green]Available[/green]" if state == "Available" else "[red]Shutdown[/red]"
        table.add_row(
            row["NAME"],
            row["REPOSITORY"],
            state_style,
            row["CREATED"],
            row["LAST USED"]
        )
    
    console.print(table)
