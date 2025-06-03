---
layout: default.md
title: Schedule
---
<div class="bg-image" style="background: url('../_img/background_imgs/brisbane_2.jpg') no-repeat center center/cover;"></div>

<!-- Added floating credits for background photo -->
<div class="photo-credits">
  Background photo by
  <a href="https://flic.kr/p/dSDFnK" target="_blank" rel="noopener">Andrew S.</a>
  distributed under a
  <a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener"><i class="fab fa-creative-commons"></i><i class="fa-brands fa-creative-commons-by"></i><i class="fa-brands fa-creative-commons-sa"></i></a>
  CC BY-SA 2.0 license.
</div>

<section class="content">

<div class="schedule-container">

<style>
.schedule-container table {
  font-size: 0.9em;
  border-collapse: collapse;
  width: 100%;
}

.schedule-container td, .schedule-container th {
  padding: 8px 4px;
  text-align: center;
  vertical-align: middle;
  border: 1px solid #ddd;
}

.schedule-container th {
  background-color: #f5f5f5;
  font-weight: bold;
}

/* Reset any default table styling that might interfere */
.schedule-container table tr:nth-child(even) td,
.schedule-container table tr:nth-child(odd) td {
  background-color: transparent !important;
  background: transparent !important;
}

/* Override global table styles for schedule */
.schedule-container table tr td {
  background: transparent !important;
}

.schedule-container table tr:hover td {
  background: transparent !important;
}

/* Activity type styling - using !important to override any inherited styles */
.activity-brainhack { background-color: #e3f2fd !important; color: #1565c0 !important; font-weight: bold; }
.activity-welcome { background-color: #f3e5f5 !important; color: #7b1fa2 !important; font-weight: bold; }
.activity-pitch { background-color: #fff3e0 !important; color: #ef6c00 !important; font-weight: bold; }
.activity-opening { background-color: #fdf2e4 !important; color: #e65100 !important; font-weight: bold; }
.activity-reports { background-color: #ede7f6 !important; color: #512da8 !important; font-weight: bold; }
.activity-closing { background-color: #ffebee !important; color: #d32f2f !important; font-weight: bold; }
.activity-sponsor { background-color: #fff8e1 !important; color: #f57f17 !important; }
.activity-hacktrack { background-color: #e8f5e8 !important; color: #2e7d32 !important; }
.activity-neurodesk { background-color: #fce4ec !important; color: #c2185b !important; }
.activity-neurostat { background-color: #e1f5fe !important; color: #0277bd !important; }
.activity-traintrack { background-color: #f1f8e9 !important; color: #558b2f !important; }
.activity-break { background-color: #f0f0f0 !important; color: #666 !important; font-weight: bold; }

/* Ensure empty cells stay neutral */
.schedule-container td:empty {
  background-color: transparent !important;
  background: transparent !important;
}

/* Force activity colors to override any inherited styles */
.schedule-container tr td.activity-brainhack,
.schedule-container tr td.activity-welcome,
.schedule-container tr td.activity-pitch,
.schedule-container tr td.activity-opening,
.schedule-container tr td.activity-reports,
.schedule-container tr td.activity-closing,
.schedule-container tr td.activity-sponsor,
.schedule-container tr td.activity-hacktrack,
.schedule-container tr td.activity-neurodesk,
.schedule-container tr td.activity-neurostat,
.schedule-container tr td.activity-traintrack,
.schedule-container tr td.activity-break {
  background: var(--activity-bg-color) !important;
  color: var(--activity-text-color) !important;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const cells = document.querySelectorAll('.schedule-container td');
  
  cells.forEach(cell => {
    const text = cell.textContent.trim();
    
    // Only apply styling to cells with actual content
    if (text.length === 0) {
      return; // Skip empty cells
    }
    
    if (text.includes('BrainHack 101')) {
      cell.classList.add('activity-brainhack');
    } else if (text.includes('Welcome & Info')) {
      cell.classList.add('activity-welcome');
    } else if (text.includes('Project pitch')) {
      cell.classList.add('activity-pitch');
    } else if (text.includes('Opening session')) {
      cell.classList.add('activity-opening');
    } else if (text.includes('Project reports')) {
      cell.classList.add('activity-reports');
    } else if (text.includes('Closing remarks')) {
      cell.classList.add('activity-closing');
    } else if (text.includes('Hacktrack / Sponsor sessions')) {
      cell.classList.add('activity-sponsor');
    } else if (text.includes('NeuroDesk Workshop')) {
      cell.classList.add('activity-neurodesk');
    } else if (text.includes('Neuroimaging Statistics Workshop')) {
      cell.classList.add('activity-neurostat');
    } else if (text.includes('TrainTrack')) {
      cell.classList.add('activity-traintrack');
    } else if (text.includes('Hacktrack') && !text.includes('Sponsor')) {
      cell.classList.add('activity-hacktrack');
    } else if (text.includes('Lunch') || text.includes('Coffee break')) {
      cell.classList.add('activity-break');
    }
  });
});
</script>

# Schedule

## Day 1 - June 21, 2025
  
| Time          | Stair Stadium (150 seated) | DIMBIN-Mil Seminar Room (60 seated) | WARRAR ROOM (30 seated) | Launch Event Space (80 seated) |
|---------------|---------------------------|--------------------------------------|--------------------------|-------------------------------|
| 08:00 - 08:30 | BrainHack 101 | | | |
| 08:30 - 09:00 | BrainHack 101 | | | |
| 09:00 - 09:30 | Welcome & Info | | | |
| 09:30 - 10:00 | Project pitch | | | |
| 10:00 - 10:30 | Project pitch | | | |
| 10:30 - 11:00 | Project pitch | | | |
| 11:00 - 11:30 | Hacktrack / Sponsor sessions | | | NeuroDesk Workshop |
| 11:30 - 12:00 | Hacktrack / Sponsor sessions | | | NeuroDesk Workshop |
| 12:00 - 12:30 | Lunch | Lunch | Lunch | Lunch |
| 12:30 - 13:00 | Lunch | Lunch | Lunch | Lunch |
| 13:00 - 13:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 13:30 - 14:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 14:00 - 14:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 14:30 - 15:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 15:00 - 15:30 | Coffee break | Coffee break | Coffee break | Coffee break |
| 15:30 - 16:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 16:00 - 16:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 16:30 - 17:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 17:00 - 17:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |
| 17:30 - 19:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | NeuroDesk Workshop |


## Day 2 - June 22, 2025
  
| Time          | Stair Stadium (150 seated) | DIMBIN-Mil Seminar Room (60 seated) | WARRAR ROOM (30 seated) | Launch Event Space (80 seated) |
|---------------|---------------------------|--------------------------------------|--------------------------|-------------------------------|
| 08:00 - 08:30 | | | | |
| 08:30 - 09:00 | | | | |
| 09:00 - 09:30 | Opening session | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 09:30 - 10:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 10:00 - 10:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 10:30 - 11:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 11:00 - 11:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 11:30 - 12:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 12:00 - 12:30 | Lunch | Lunch | Lunch | Lunch |
| 12:30 - 13:00 | Lunch | Lunch | Lunch | Lunch |
| 13:00 - 13:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 13:30 - 14:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 14:00 - 14:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 14:30 - 15:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 15:00 - 15:30 | Coffee break | Coffee break | Coffee break | Neuroimaging Statistics Workshop |
| 15:30 - 16:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 16:00 - 16:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 16:30 - 17:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 17:00 - 17:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 17:30 - 19:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |


## Day 3 - June 23, 2025

| Time          | Stair Stadium (150 seated) | DIMBIN-Mil Seminar Room (60 seated) | WARRAR ROOM (30 seated) | Launch Event Space (80 seated) |
|---------------|---------------------------|--------------------------------------|--------------------------|-------------------------------|
| 08:00 - 08:30 | | | | |
| 08:30 - 09:00 | | | | |
| 09:00 - 09:30 | Opening session | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 09:30 - 10:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 10:00 - 10:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 10:30 - 11:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 11:00 - 11:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 11:30 - 12:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | Neuroimaging Statistics Workshop |
| 12:00 - 12:30 | Lunch | Lunch | Lunch | Neuroimaging Statistics Workshop |
| 12:30 - 13:00 | Lunch | Lunch | Lunch | Lunch |
| 13:00 - 13:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 13:30 - 14:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 14:00 - 14:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 14:30 - 15:00 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 15:00 - 15:30 | Hacktrack / Sponsor sessions | Hacktrack | Hacktrack | TrainTrack / Unconferences |
| 15:30 - 16:00 | Coffee break | Coffee break | Coffee break | Coffee break |
| 16:00 - 16:30 | Project reports | | | |
| 16:30 - 17:00 | Project reports | | | |
| 17:00 - 17:30 | Project reports | | | |
| 17:30 - 18:00 | Closing remarks | | | |

</div>

</section>
