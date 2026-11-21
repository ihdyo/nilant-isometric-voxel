# Voxel Fauna · Publish Log

Every upload event, newest at the bottom, the way Nilant's workbook records each upload in its Schedule. Written by
`python _system/studio/scripts/vf.py log <code or Image ID> <platform> <action> [--link URL] [--note "..."]`, which also
adds the row to the platform's workbook (`05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx`, Publish Log) and sets
the item's State there. Actions: Submitted, Accepted, Rejected, Live, Removed, Updated. Note refusal reasons: they
shape the next uploads.

| Date | Image ID | Animal | Platform | Action | Link or platform ID | Note |
|---|---|---|---|---|---|---|
