from __future__ import annotations

from typing import Optional

from solana.transaction import TransactionInstruction, Transaction
from .constants import COMPUTE_BUDGET_ID
from .elf_params import ElfParams
from typing import Union
from .web3 import NeonWeb3


class ComputeBudget:
    @staticmethod
    def requestUnits(units, additional_fee) -> TransactionInstruction:
        return TransactionInstruction(
            program_id=COMPUTE_BUDGET_ID,
            keys=[],
            data=bytes.fromhex("00") + units.to_bytes(4, "little") + additional_fee.to_bytes(4, "little")
        )

    @staticmethod
    def requestHeapFrame(heap_frame) -> TransactionInstruction:
        return TransactionInstruction(
            program_id=COMPUTE_BUDGET_ID,
            keys=[],
            data=bytes.fromhex("01") + heap_frame.to_bytes(4, "little")
        )


class TransactionWithComputeBudget(Transaction):
    def __init__(self, proxy: NeonWeb3, compute_units: Optional[int] = None, *args, **kwargs):
        Transaction.__init__(self, *args, **kwargs)
        compute_units = compute_units if compute_units is not None else ElfParams(proxy).neon_compute_units
        additional_fee = ElfParams(proxy).neon_additional_fee
        self.instructions.append(ComputeBudget.requestUnits(compute_units, additional_fee))
        heap_frame = ElfParams(proxy).neon_heap_frame
        self.instructions.append(ComputeBudget.requestHeapFrame(heap_frame))

    def add(self, *args: Union[Transaction, TransactionInstruction]) -> TransactionWithComputeBudget:
        """Add one or more instructions to this Transaction."""
        for arg in args:
            if isinstance(arg, Transaction):
                for ix in arg.instructions:
                    if ix.program_id == COMPUTE_BUDGET_ID:
                        continue
                    else:
                        self.instructions.append(ix)
            elif isinstance(arg, TransactionInstruction):
                self.instructions.append(arg)
            else:
                raise ValueError("invalid instruction:", arg)

        return self
