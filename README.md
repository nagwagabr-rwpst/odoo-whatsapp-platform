# RWPST RelayRuntime

Replay-safe operational messaging runtime for Odoo.

RelayRuntime provides resilient campaign execution, lease-aware orchestration, replay-safe recovery, and operational observability for large-scale messaging workflows in Odoo.

### Core Runtime Capabilities

- Replay-safe execution recovery
- Lease-aware batch orchestration
- Execution lineage and retry tracking
- Operational observability and diagnostics
- Runtime-safe campaign processing

---

## Runtime Trust Layer

Built for resilient operational workflows with replay-safe recovery, lease-aware coordination, execution lineage tracking, and runtime observability.

## Architecture Direction

RelayRuntime is designed as a platform-oriented execution runtime delivered initially as an Odoo application.

The current architecture embeds runtime coordination inside Odoo while preparing clear boundaries for future worker extraction, runtime isolation, and operational scaling.

## Why RelayRuntime Exists

Operational messaging workflows become significantly more complex once execution failures, retries, partial delivery states, and long-running batch operations are introduced.

Traditional messaging integrations often optimize for happy-path delivery while leaving operational recovery, execution consistency, and replay safety undefined.

RelayRuntime was designed to address operational runtime concerns such as:

- Duplicate execution corruption during retries
- Unsafe replay behavior after interrupted batches
- Stale execution states after worker or process failure
- Attachment coordination inconsistencies
- Missing operational visibility during long-running campaigns
- Recovery ambiguity after partial execution completion
The project focuses on execution correctness, replay-safe recovery, operational observability, and resilient orchestration rather than simple message delivery automation.

---
## Failure-First Runtime Thinking

RelayRuntime is designed around the assumption that operational failures are inevitable in long-running messaging workflows.

Execution interruptions, provider instability, partial batch completion, stale runtime states, network failures, and retry ambiguity are treated as normal operational conditions rather than exceptional edge cases.

Instead of optimizing exclusively for successful delivery flows, the runtime prioritizes:

- Recovery-aware execution behavior
- Replay-safe orchestration
- Execution lineage tracking
- Lease-aware coordination
- Failure diagnostics and operational visibility
- Runtime consistency during partial execution states

This philosophy influences the runtime lifecycle, retry behavior, reconciliation logic, and future worker extraction strategy.

## Replay-Safe Recovery

RelayRuntime treats recovery as a controlled runtime operation rather than a blind retry mechanism.

When execution interruptions occur, the runtime attempts to preserve execution consistency by tracking execution lineage, retry relationships, lease ownership, and partial completion states.

Replay-aware recovery behavior is designed to reduce risks such as:

- Duplicate execution during interrupted retries
- Inconsistent batch completion states
- Reprocessing ambiguity after partial execution
- Recovery conflicts caused by stale runtime ownership
- Attachment replay inconsistencies

The runtime currently provides replay-aware orchestration within an embedded Odoo execution model while preparing architectural boundaries for future worker isolation and external runtime coordination.

RelayRuntime does not claim exactly-once distributed execution guarantees.

Instead, the project focuses on operationally safe recovery behavior, replay-aware execution coordination, and execution-state observability within the constraints of the current architecture.

## Execution Lifecycle

RelayRuntime organizes operational messaging flows around explicit execution lifecycle stages rather than isolated send actions.

A typical runtime flow follows the sequence below:

```text
Campaign
    ↓
Batch Preparation
    ↓
Lease Acquisition
    ↓
Execution Start
    ↓
Delivery Processing
    ↓
Retry Evaluation
    ↓
Replay / Recovery
    ↓
Execution Completion
```

---
## Operational Observability

RelayRuntime emphasizes operational visibility throughout the execution lifecycle in order to reduce ambiguity during long-running or partially interrupted messaging operations.

The runtime tracks execution-oriented operational signals such as:

* Execution state transitions
* Retry and replay lineage
* Lease ownership and recovery conditions
* Partial batch completion visibility
* Delivery processing diagnostics
* Runtime reconciliation behavior

Operational observability is intended to support:

* Failure investigation
* Recovery analysis
* Replay diagnostics
* Runtime inspection
* Future worker/runtime coordination

The current architecture provides embedded observability inside the Odoo execution model while preparing boundaries for future runtime isolation and external telemetry evolution.
