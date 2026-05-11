#!/usr/bin/env python3
"""
Verificación técnica de posts contra base de datos GElectrical (IEC).

Uso:
    python3 agente/verificar.py cable          # Verifica datos de cables IEC
    python3 agente/verificar.py cb             # Verifica magnetotérmicos (curvas B/C/D)
    python3 agente/verificar.py motor          # Verifica parámetros de motores
    python3 agente/verificar.py transformer    # Verifica transformadores
    python3 agente/verificar.py all            # Muestra resumen de todas las bases de datos

Fuente: referencias/GElectrical/gelectrical/database/
Repo:   https://github.com/manuvarkey/GElectrical
"""

import sys
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'referencias', 'GElectrical', 'gelectrical', 'database')


def read_csv(filename):
    path = os.path.join(DB_PATH, filename)
    if not os.path.exists(path):
        print(f"ERROR: No se encuentra {path}")
        print("Ejecuta: git submodule update --init --recursive")
        sys.exit(1)
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def cmd_cable():
    rows = read_csv('cable_iec.csv')
    print("=" * 70)
    print("BASE DE DATOS IEC — CABLES (cable_iec.csv)")
    print("Fuente: GElectrical / UNE-HD 60364-5-52")
    print("=" * 70)
    # Agrupar por material y aislamiento
    by_type = {}
    for r in rows:
        key = f"{r['conductor_material']} / {r['insulation_material']} / {r['type_of_cable']}"
        by_type.setdefault(key, []).append(r)

    for group, cables in sorted(by_type.items()):
        print(f"\n  {group}")
        print(f"  {'Designación':<20} {'Secc.(mm²)':>10} {'X(Ω/km)':>10} {'C(nF/km)':>10}")
        print(f"  {'-'*55}")
        for c in sorted(cables, key=lambda x: float(x['conductor_cross_section'])):
            print(f"  {c['designation']:<20} {c['conductor_cross_section']:>10} "
                  f"{c['x_ohm_per_km']:>10} {c['c_nf_per_km']:>10}")


def cmd_cb():
    rows = read_csv('cb.csv')
    print("=" * 70)
    print("BASE DE DATOS IEC — MAGNETOTÉRMICOS / MCB (cb.csv)")
    print("Fuente: GElectrical / IEC 60898-1")
    print("=" * 70)

    # Filtrar MCBs estándar (no customizados)
    mcbs = [r for r in rows if 'MCB' in r.get('type', '') or 'MCB' in r.get('subtype', '')]
    by_curve = {}
    for r in mcbs:
        curve = r.get('prot_curve_type', 'Unknown')
        by_curve.setdefault(curve, []).append(r)

    for curve, items in sorted(by_curve.items()):
        print(f"\n  Curva: {curve}")
        print(f"  {'Nombre':<30} {'In (A)':>8} {'Isc (kA)':>10} {'Categoría':<20}")
        print(f"  {'-'*70}")
        seen = set()
        for item in sorted(items, key=lambda x: float(x.get('In', 0))):
            key = (item.get('In'), curve, item.get('item_category', '')[:20])
            if key not in seen:
                seen.add(key)
                print(f"  {item['item_name']:<30} {item.get('In','?'):>8} "
                      f"{item.get('Isc','?'):>10} {item.get('item_category','')[:20]:<20}")


def cmd_motor():
    rows = read_csv('motor.csv')
    print("=" * 70)
    print("BASE DE DATOS IEC — MOTORES TRIFÁSICOS (motor.csv)")
    print("Fuente: GElectrical / IEC 60034")
    print("=" * 70)
    if rows:
        headers = list(rows[0].keys())
        print(f"\n  Campos disponibles: {', '.join(headers)}")
        print(f"\n  {'Nombre':<25} ", end="")
        for h in headers[1:6]:
            print(f"{h[:12]:>12}", end="")
        print()
        print(f"  {'-'*80}")
        for r in rows[:20]:
            print(f"  {r[headers[0]][:25]:<25} ", end="")
            for h in headers[1:6]:
                print(f"{str(r.get(h,''))[:12]:>12}", end="")
            print()
        if len(rows) > 20:
            print(f"  ... ({len(rows) - 20} filas más)")


def cmd_transformer():
    rows = read_csv('transformer.csv')
    print("=" * 70)
    print("BASE DE DATOS IEC — TRANSFORMADORES (transformer.csv)")
    print("Fuente: GElectrical / IEC 60076")
    print("=" * 70)
    if rows:
        headers = list(rows[0].keys())
        print(f"\n  Campos disponibles: {', '.join(headers)}")
        print(f"\n  {'Nombre':<30} ", end="")
        for h in headers[1:5]:
            print(f"{h[:12]:>12}", end="")
        print()
        print(f"  {'-'*80}")
        for r in rows[:15]:
            print(f"  {r[headers[0]][:30]:<30} ", end="")
            for h in headers[1:5]:
                print(f"{str(r.get(h,''))[:12]:>12}", end="")
            print()


def cmd_all():
    dbs = {
        'cable_iec.csv': 'Cables IEC (secciones, materiales, reactancias)',
        'cb.csv':        'Magnetotérmicos MCB/MCCB/ACB (curvas B/C/D, calibres)',
        'fuse.csv':      'Fusibles (calibres, tipo gG/aM)',
        'motor.csv':     'Motores trifásicos IEC',
        'motor1ph.csv':  'Motores monofásicos',
        'transformer.csv':   'Transformadores IEC 60076',
        'transformer3w.csv': 'Transformadores trifásicos 3 devanados',
        'line.csv':      'Líneas aéreas/subterráneas (R, X por km)',
        'line_busbar.csv':   'Barras colectoras',
    }
    print("=" * 70)
    print("RESUMEN — BASE DE DATOS GElectrical (IEC)")
    print(f"Ruta: {os.path.abspath(DB_PATH)}")
    print("=" * 70)
    for fname, desc in dbs.items():
        try:
            rows = read_csv(fname)
            print(f"  ✓  {fname:<25} {len(rows):>4} registros  —  {desc}")
        except SystemExit:
            print(f"  ✗  {fname:<25}   (no disponible)")

    print()
    print("Comandos de consulta:")
    print("  python3 agente/verificar.py cable")
    print("  python3 agente/verificar.py cb")
    print("  python3 agente/verificar.py motor")
    print("  python3 agente/verificar.py transformer")

    # Mostrar commit actual del submodule
    submodule_git = os.path.join(DB_PATH, '..', '..', '..', '.git', 'HEAD')
    ge_git = os.path.join(DB_PATH, '..', '..', '.git', 'HEAD')
    try:
        with open(ge_git) as f:
            ref = f.read().strip()
        print(f"\nSubmodule GElectrical HEAD: {ref}")
    except Exception:
        pass


COMMANDS = {
    'cable': cmd_cable,
    'cb': cmd_cb,
    'motor': cmd_motor,
    'transformer': cmd_transformer,
    'all': cmd_all,
}

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if cmd not in COMMANDS:
        print(f"Comando desconocido: {cmd}")
        print(f"Comandos válidos: {', '.join(COMMANDS)}")
        sys.exit(1)
    COMMANDS[cmd]()
