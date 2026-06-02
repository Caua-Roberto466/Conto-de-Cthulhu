# 🐙 Conto de Cthulhu

> *"A humanidade mais misericordiosa do mundo é a incapacidade da mente humana de correlacionar todo o seu conteúdo."*
> — H.P. Lovecraft

RPG de terminal em Python ambientado no universo de Lovecraft. Enfrente criaturas além da compreensão humana, preserve sua sanidade e descubra a verdade sobre o **Grande Cthulhu** — antes que ele desperte.

---

## 🗂️ Sumário

- [Sobre o jogo](#-sobre-o-jogo)
- [Como jogar](#-como-jogar)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Classes disponíveis](#-classes-disponíveis)
- [Sistema de combate](#️-sistema-de-combate)
- [Atributos](#-atributos)
- [Efeitos de status](#-efeitos-de-status)
- [Sistema de XP e nível](#-sistema-de-xp-e-nível)
- [Como rodar](#-como-rodar)
- [Tecnologias](#-tecnologias)
- [Roadmap](#-roadmap)

---

## 📖 Sobre o jogo

Conto de Cthulhu é um RPG por turnos jogado inteiramente no terminal. Você escolhe um personagem principal e percorre áreas sombrias inspiradas no universo lovecraftiano, encontrando aliados, enfrentando criaturas e acumulando conhecimento proibido.

Cada personagem tem sua própria história, área de início e conjunto único de habilidades. O objetivo final é reunir um time de 4 aliados, atravessar as masmorras e enfrentar o **Cthulhu** no confronto final.

---

## 🎮 Como jogar

1. Escolha seu personagem principal — cada um começa em um local diferente com sua própria história.
2. Complete a área inicial sozinho.
3. Ao avançar, você encontrará outros personagens e poderá convidá-los para o seu time.
4. Com 4 aliados reunidos, entre nas masmorras — cada uma tem seu próprio boss e avança a narrativa.
5. Complete todas as masmorras e enfrente o Cthulhu no confronto final.

### Ações em combate

Em cada turno, o jogador pode escolher uma ação para cada herói:

| Opção | Ação | Descrição |
|-------|------|-----------|
| `1` | **Atacar** | Ataque básico com a arma do personagem |
| `2` | **Usar habilidade** | Usa uma das 3 habilidades da classe |
| `3` | **Defender** | Aumenta a defesa em +10 até o próximo turno |
| `4` | **Usar item** | Usa um item do inventário *(em desenvolvimento)* |
| `5` | **Fugir** | Tenta escapar do combate *(em desenvolvimento)* |

---

## 🗃️ Estrutura do projeto

```
Conto-de-Cthulhu/
│
├── main.py                      # Ponto de entrada do jogo
│
├── personagens/
│   ├── personagem.py            # Classes base: Personagem, Herois, Habilidade
│   ├── rafael.py                # Alienista
│   ├── caio.py                  # Coveiro
│   ├── claudia.py               # Ocultista
│   └── douglas.py               # Investigador
│
├── monstros/
│   ├── monstro.py               # Classe base dos monstros
│   └── doutrinador.py           # Monstro: Doutrinador
│
├── combate/
│   ├── batalha.py               # Loop principal de combate
│   └── vitoria.py               # Distribuição de XP pós-batalha
│
├── interface/
│   └── cores.py                 # Códigos ANSI de cores para o terminal
│
└── livros/                      # Itens e livros do jogo (em desenvolvimento)
```

---

## 🧙 Classes disponíveis

### 🔬 Alienista — *Rafael*
> *"Médico do hospício, tem uma mente forte contra todo o horror da vida."*

Ataca com **Equipamentos Médicos**. Especialista em debuffs e recuperação de sanidade.

**Passiva — Mente Blindada:** Toda vez que ele ou algum membro da equipe perder sanidade, recupera 5 dela.

| # | Habilidade | Custo | Efeito |
|---|-----------|-------|--------|
| 1 | Sedativo | 15 | Aplica tranquilizante: reduz ataque e defesa do inimigo |
| 2 | Terapia de Choque | 30 | Dano elétrico com chance de crítico |
| 3 | Trabalho Mental | 60 | Restaura totalmente a própria sanidade |

---

### ⚰️ Coveiro — *Caio*
> *"Anos trabalhando no cemitério fez ele se familiarizar com a morte."*

Ataca com **Pá de Ferro**. Alto dano físico, bom sustento em combate.

**Passiva — Olhar de Cadáver:** Imune a efeitos de medo e insanidade.

| # | Habilidade | Custo | Efeito |
|---|-----------|-------|--------|
| 1 | Corte de Defunto | 15 | Corte rápido com a pá causando sangramento |
| 2 | Giro do Coveiro | 20 | Ataque giratório de alto impacto |
| 3 | Enterro Marcado | 50 | Pancada letal garantindo acerto crítico |

---

### 🔮 Ocultista — *Claudia*
> *"Forte conexão com o além-vida e conhecimento de rituais antigos."*

Ataca conjurando **Rituais Antigos**. Maior poder ofensivo, mas frágil fisicamente.

**Passiva — Sexto Sentido:** Aumenta a chance de crítico em todas as habilidades.

| # | Habilidade | Custo | Efeito |
|---|-----------|-------|--------|
| 1 | Olhar do Vazio | 20 | Reduz a defesa do inimigo por 3 turnos |
| 2 | Chamas do Vácuo | 40 | Dano + queimadura por 5 turnos |
| 3 | Ritual de Sangue | 80 | Dano massivo em área — custa metade da própria vida |

---

### 🔍 Investigador — *Douglas*
> *"Já capturou diversos criminosos pelas ruas de Londres."*

Ataca com **Revólver Webley**. Alta precisão e chance de crítico elevada.

**Passiva — Instinto de Londres:** Elimina a chance de errar ataques.

| # | Habilidade | Custo | Efeito |
|---|-----------|-------|--------|
| 1 | Investigar | 10 | Revela a fraqueza do inimigo |
| 2 | Coronhada | 25 | Ataque com alta chance de crítico |
| 3 | Tiro Duplo | 50 | Dois tiros que causam o dobro de dano |

---

### ⚓ Marujo *(em desenvolvimento)*
> *"Anos no porto lhe garantiram um porte físico imponente."*

Ataca com **Arpão**. Tanque do grupo com boa resistência a dano.

**Passiva — Pele de Sal:** Reduz todo dano recebido.

---

### 🏺 Arqueólogo *(em desenvolvimento)*
> *"Explora locais antigos em busca de pistas sobre o Cthulhu."*

Ataca com a **Garra de Mi-Go**. Controle de grupo e dano em área.

**Passiva — Vontade de Aço:** Todo o time fica imune a hipnose.

---

### 🏥 Enfermeiro *(em desenvolvimento)*
> *"Anos de hospital lhe deram habilidades médicas incríveis."*

Ataca com **Bisturi**. Curandeiro do grupo.

**Passiva — Vacina Anti-Morte:** Imune a efeitos físicos negativos.

---

## ⚔️ Sistema de combate

O combate é por turnos com estrutura em duas fases:

```
FASE DOS HERÓIS
  └── Cada herói age uma vez (na ordem do time)
      └── Escolhe: Atacar / Habilidade / Defender / Item / Fugir

FASE DOS MONSTROS
  └── Cada monstro ataca um herói aleatório
      └── Monstros com dano de sanidade acionam passivas do time
```

### Cálculo de dano

```
Dano final = Ataque × modificador − (Ataque × modificador - Defesa)
Crítico    = Dano × 1.2
Mínimo     = 1 (nunca causa 0 de dano em acerto)
```

### Passivas automáticas

As passivas são acionadas automaticamente pelo sistema de combate via eventos. Quando um personagem perde sanidade, por exemplo, todos os heróis do time são notificados e cada um reage de acordo com sua passiva.

---

## 📊 Atributos

| Atributo | Descrição |
|----------|-----------|
| **Vida** | Pontos de vida — ao chegar a 0 o personagem é derrotado |
| **Sanidade** | Resistência ao horror — ao chegar a 0 o personagem enlouquece |
| **Energia** | Recurso gasto para usar habilidades |
| **Ataque** | Base de dano dos ataques e habilidades |
| **Defesa** | Reduz o dano recebido (em %) |
| **Precisão** | Chance de acertar um ataque (0–100) |
| **Chance de crítico** | Chance de causar dano aumentado no acerto |

---

## 🌀 Efeitos de status

Efeitos são aplicados por habilidades e processados automaticamente no início de cada turno. Cada efeito tem duração em turnos e reverte seus modificadores ao expirar.

| Efeito | Origem | Impacto |
|--------|--------|---------|
| **Sedativo** | Alienista | −3 Ataque, −3 Defesa por 3 turnos |
| **Intimidação** | Ocultista | −6 Defesa por 3 turnos |
| **Queimadura** | Ocultista | 15 de dano por turno durante 5 turnos |
| **Sangramento** | Coveiro / Arqueólogo | Dano contínuo por turnos *(em desenvolvimento)* |

---

## 📈 Sistema de XP e nível

Ao derrotar monstros, todos os heróis do time ganham XP. O XP necessário aumenta 10% a cada nível.

```
Nível 1 → 2:  100 XP
Nível 2 → 3:  110 XP
Nível 3 → 4:  121 XP
... e assim por diante
```

### Ganhos por nível

| Atributo | Crescimento |
|----------|-------------|
| Vida máxima | +10 |
| Ataque | ×1.2 |
| Defesa | ×1.1 |
| Energia | ×1.1 |
| Sanidade máxima | ×1.01 |

A vida e sanidade são restauradas completamente ao subir de nível.

---

## 🚀 Como rodar

**Pré-requisitos:** Python 3.10+

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Conto-de-Cthulhu.git
cd Conto-de-Cthulhu

# Rode o jogo a partir da raiz do projeto
python3 main.py
```

> ⚠️ **Importante:** sempre rode a partir da pasta raiz do projeto. Rodar arquivos individuais diretamente pode causar erros de importação.

---

## 🛠️ Tecnologias

- **Python 3.10+** — linguagem principal
- **POO (Programação Orientada a Objetos)** — toda a arquitetura do jogo usa herança, polimorfismo e encapsulamento
- **Módulo `random`** — sistema de dados para combate
- **Módulo `time`** — delays para ritmo narrativo
- **Códigos ANSI** — cores no terminal via `interface/cores.py`

---

## 🗺️ Roadmap

- [x] Sistema de combate por turnos
- [x] Sistema de passivas com eventos
- [x] Sistema de efeitos de status com duração
- [x] Sistema de XP e level up
- [x] Cores no terminal
- [x] Alienista, Coveiro, Ocultista, Investigador implementados
- [ ] Arqueólogo, Marujo e Enfermeiro
- [ ] Sistema de itens e inventário
- [ ] Opção de fuga do combate
- [ ] Masmorras e progressão de mapa
- [ ] Diálogos e narrativa por área
- [ ] Boss final — Cthulhu
- [ ] Menu principal e seleção de personagem

---

*Feito com 🐙 e uma pitada de insanidade cósmica.*
