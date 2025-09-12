<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>allplan-cz\Rearange_reinf.py</Name>
        <Title>Přečíslování výztuže dle tvaru</Title>
        <TextId>100</TextId>
        <Interactor>False</Interactor>
        <Version>0.1.0</Version>
        <ShowFavoriteButtons>True</ShowFavoriteButtons>
        <ReadLastInput>True</ReadLastInput>
    </Script>
    <Page>
        <Name>Reinf</Name>
        <Text>reinf</Text>

            <Parameter>
                <Name>starting_mark_number_straight</Name>
                <Text>Přímé pruty od č.</Text>
                <TextId>1001</TextId>
                <Value>100</Value>
                <ValueType>Integer</ValueType>
            </Parameter>


            <Parameter>
                <Text>Seřadit dle délky</Text>
                <TextId>1002</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky od nejkratší po nejdelší</Text>
                    <TextId>1003</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>sorting_straight</Name>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Constraint>sorting_straight_diameter</Constraint>
                </Parameter>
            </Parameter>

            <Parameter>
                <Text>Seřadit dle průměru a délky</Text>
                <TextId>1004</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky nejprve podle průměru a poté podle délky</Text>
                    <TextId>1005</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>sorting_straight_diameter</Name>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Constraint>sorting_straight</Constraint>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>lock_straight</Name>
                <Text>Zablokování</Text>
                <TextId>1006</TextId>
                <Value>False</Value>
                <Visible>True</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>round_straight</Name>
                <Text>Zaokrouhlení</Text>
                <TextId>1007</TextId>
                <Value>1</Value>
                <Visible>True</Visible>
                <ValueType>Length</ValueType>
            </Parameter>

            <Parameter>
                <Name>identical_prefix_straight</Name>
                <Text>Text před</Text>
                <TextId>1008</TextId>
                <Value>False</Value>
                <Visible>False</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>ButtonRow1</Name>
                <Text>Přímé pruty</Text>
                <TextId>1009</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje pouze přímé pruty a seřadí je od zadaného čísla</Text>
                    <TextId>1010</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>

                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat</Text>
                    <TextId>1011</TextId>
                    <EventId>1001</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>
            <Parameter>
                <Name>ButtonRow1</Name>
                <Text></Text>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje a sjednotí pouze přímé pruty a seřadí je od zadaného čísla</Text>
                    <TextId>1012</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button1</Name>
                    <Text>Přečíslovat a sjednotit</Text>
                    <TextId>1013</TextId>
                    <EventId>1011</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>


            <Parameter>
                <Name>Separator</Name>
                <ValueType>Separator</ValueType>
            </Parameter>

            <Parameter>
                <Name>starting_mark_number_bend</Name>
                <Text>Ohýbané pruty od č.</Text>
                <TextId>1014</TextId>
                <Value>200</Value>
                <ValueType>Integer</ValueType>
            </Parameter>

            <Parameter>
                <Name>sorting_bend</Name>
                <Text>Seřadit dle délky</Text>
                <TextId>1002</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky od nejkratší po nejdelší</Text>
                    <TextId>1003</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>sorting_bend</Name>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Constraint>sorting_bend_diameter</Constraint>
                </Parameter>
            </Parameter>

            <Parameter>
                <Text>Seřadit dle průměru a délky</Text>
                <TextId>1004</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky nejprve podle průměru a poté podle délky</Text>
                    <TextId>1005</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>sorting_bend_diameter</Name>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Constraint>sorting_bend</Constraint>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>lock_bend</Name>
                <Text>Zablokování</Text>
                <TextId>1006</TextId>
                <Value>False</Value>
                <Visible>True</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>round_bend</Name>
                <Text>Zaokrouhlení</Text>
                <TextId>1007</TextId>
                <Value>1</Value>
                <Visible>True</Visible>
                <ValueType>Length</ValueType>
            </Parameter>

            <Parameter>
                <Name>identical_prefix_bend</Name>
                <Text>Text před</Text>
                <TextId>1008</TextId>
                <Value>False</Value>
                <Visible>False</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Ohýbané pruty</Text>
                <TextId>1015</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje pouze ohýbané pruty a seřadí je od zadaného čísla</Text>
                    <TextId>1016</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat</Text>
                    <TextId>1011</TextId>
                    <EventId>1002</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>
            <Parameter>
                <Name>ButtonRow</Name>
                <Text></Text>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje a sjednotí pouze ohýbané pruty a seřadí je od zadaného čísla</Text>
                    <TextId>1017</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat a sjednotit</Text>
                    <TextId>1013</TextId>
                    <EventId>1012</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>Separator</Name>
                <ValueType>Separator</ValueType>
            </Parameter>


            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Vše</Text>
                <TextId>1018</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje veškeré pruty a seřadí je od zadaného čísla</Text>
                    <TextId>1019</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat vše dle nastavení</Text>
                    <TextId>1020</TextId>
                    <EventId>1000</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>Separator</Name>
                <ValueType>Separator</ValueType>
            </Parameter>

            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Přečíslovat vše dle tvaru</Text>
                <TextId>1021</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečíslovat vše dle tvaru</Text>
                    <TextId>1021</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat</Text>
                    <TextId>1011</TextId>
                    <EventId>3000</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Dočasné přečíslování</Text>
                <TextId>1022</TextId>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Slouží k dočasnému přesunutí prutů na vysoké pozice aby se zamezilo kolizím při přečíslování</Text>
                    <TextId>1023</TextId>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat (9000)</Text>
                    <TextId>1024</TextId>
                    <EventId>2000</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>




        </Page>
</Element>
