<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>allplan-cz\Rearange_reinf.py</Name>
        <Title>Přečíslování výztuže dle tvaru</Title>
        <TextID>100</TextID>
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
                <TextID>1001</TextID>
                <Value>100</Value>
                <ValueType>Integer</ValueType>
            </Parameter>


            <Parameter>
                <Text>Seřadit dle délky</Text>
                <TextID>1002</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky od nejkratší po nejdelší</Text>
                    <TextID>1003</TextID>
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
                <TextID>1004</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky nejprve podle průměru a poté podle délky</Text>
                    <TextID>1005</TextID>
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
                <TextID>1006</TextID>
                <Value>False</Value>
                <Visible>True</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>round_straight</Name>
                <Text>Zaokrouhlení</Text>
                <TextID>1007</TextID>
                <Value>1</Value>
                <Visible>True</Visible>
                <ValueType>Length</ValueType>
            </Parameter>

            <Parameter>
                <Name>identical_prefix_straight</Name>
                <Text>Text před</Text>
                <TextID>1008</TextID>
                <Value>False</Value>
                <Visible>False</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>ButtonRow1</Name>
                <Text>Přímé pruty</Text>
                <TextID>1009</TextID>
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
                    <TextID>1011</TextID>
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
                    <TextID>1012</TextID>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button1</Name>
                    <Text>Přečíslovat a sjednotit</Text>
                    <TextID>1013</TextID>
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
                <TextID>1014</TextID>
                <Value>200</Value>
                <ValueType>Integer</ValueType>
            </Parameter>

            <Parameter>
                <Name>sorting_bend</Name>
                <Text>Seřadit dle délky</Text>
                <TextID>1002</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky od nejkratší po nejdelší</Text>
                    <TextID>1003</TextID>
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
                <TextID>1004</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Setřídí položky nejprve podle průměru a poté podle délky</Text>
                    <TextID>1005</TextID>
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
                <TextID>1006</TextID>
                <Value>False</Value>
                <Visible>True</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>round_bend</Name>
                <Text>Zaokrouhlení</Text>
                <TextID>1007</TextID>
                <Value>1</Value>
                <Visible>True</Visible>
                <ValueType>Length</ValueType>
            </Parameter>

            <Parameter>
                <Name>identical_prefix_bend</Name>
                <Text>Text před</Text>
                <TextID>1008</TextID>
                <Value>False</Value>
                <Visible>False</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Ohýbané pruty</Text>
                <TextID>1015</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečísluje pouze ohýbané pruty a seřadí je od zadaného čísla</Text>
                    <TextID>1016</TextID>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat</Text>
                    <TextID>1011</TextID>
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
                    <TextID>1017</TextID>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat a sjednotit</Text>
                    <TextID>1013</TextID>
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
                <TextID>1018</TextID>
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
                    <TextID>1020</TextID>
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
                <TextID>1021</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Přečíslovat vše dle tvaru</Text>
                    <TextID>1021</TextID>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat</Text>
                    <TextID>1011</TextID>
                    <EventId>3000</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>

            <Parameter>
                <Name>ButtonRow</Name>
                <Text>Dočasné přečíslování</Text>
                <TextID>1022</TextID>
                <ValueType>Row</ValueType>
                <Value>OVERALL:1</Value>
                <Parameter>
                    <Name>InfoPicture</Name>
                    <Text>Slouží k dočasnému přesunutí prutů na vysoké pozice aby se zamezilo kolizím při přečíslování</Text>
                    <TextID>1023</TextID>
                    <Value>AllplanSettings.PictResPalette.eHotinfo</Value>
                    <ValueType>Picture</ValueType>
                </Parameter>
                <Parameter>
                    <Name>Button</Name>
                    <Text>Přečíslovat (9000)</Text>
                    <TextID>1024</TextID>
                    <EventId>2000</EventId>
                    <ValueType>Button</ValueType>
                </Parameter>
            </Parameter>




        </Page>
</Element>
