<p align="center" style="padding-top:1rem">
  <a href="https://openbeta.io">
    <img alt="OpenBeta logo" src="openbeta-logo-192x192.png" width="60" />
  </a>
</p>
<h3 align="center">Open source rock climbing</h3>
<p align="center">OpenBeta is 501(c)(3) nonprofit dedicated to ensuring free and open access to rock climbing data in computer programming, research, and data science endeavors.
</p>

## User ratings
[User ratings data extracted from MountainProject](./ratings)

## USA climbing routes data

Raw data files are temporarily unavailable.  We will republish them in the near future.

## File format
Data files are in jsonlines format. 

A sample record: ([raw file](./epinephrine-sample.jsonlines))

```json
{
   "route_name":"Epinephrine",
   "grade":{
      "YDS":"5.9",
      "French":"5c",
      "Ewbanks":"17",
      "UIAA":"VI",
      "ZA":"17",
      "British":"HVS 5a"
   },
   "safety":"",
   "type":{
      "trad":true
   },
   "fa":"Jorge Urioste, Joanne Urioste, Joe Herbst, 1978",
   "description":[
      ""
   ],
   "location":"",
   "protection":[
   ],
   "metadata":{
      "left_right_seq":"23",
      "parent_lnglat":[
         -115.46652,
         36.03518
      ],
      "parent_sector":"Black Velvet Wall",
      "mp_route_id":"105732422",
      "mp_sector_id":"105732162"
   }
}
```

## How to work with the data
We recommend using Jupyter notebook and Pandas to work with the dataset.  For a more complete example, check out our [Pandas 101 tutorial](https://openbeta.substack.com/p/pandas-101-visualize-usa-rock-climbing).

```python
import pandas as pd

# load the zip file directly
# 'lines=True' indicates jsonlines format
df = pd.read_json("/Users/nacho/git/opendata/openbeta-usa-routes-aug-2020.zip", lines=True)

df.sample(5)
```

![sample data](dataset-sample.png "Sample data")

## Questions or Comments?
- Chat with the dev team on <a href="https://discord.gg/a6vuuTQxS8">Discord</a>.
- Email us: [data@openbeta.io](mailto:data@openbeta.io) 

## Support Us
OpenBeta is free because we want to make climbing information accessible for everyone. Please consider [making a donation today.](https://opencollective.com/openbeta)

## License
[Creative Commons CC0](./LICENSE)
