## Эксперименты

Перед запуском экспериментов необходимо:

1. Подготовить датасет в директории `benchmarks/raw/hr/`
2. Установить зависимости из `experiments/requirements.txt`
3. Настроить `accelerate`

```bash
pip install -r experiments/requirements.txt

accelerate config
```

---

## Структура экспериментов

```text
experiments/
├── train_stages.sh
├── test_stages.sh
└── stage/
```

---

## Exp. Bi-Encoder Retrieval

Эксперименты с базовой bi-encoder архитектурой:

- baseline без дообучения
- supervised fine-tuning retrieval модели

### Обучение

```bash
bash train_stages.sh stage1
```

### Тестирование

```bash
bash test_stages.sh stage1
```