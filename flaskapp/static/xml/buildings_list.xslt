<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <head>
        <title>Buildings</title>
    </head>
    <body>
    <ul>
        <xsl:for-each select="buildings/building">
        <li> 
            <xsl:value-of select="@id"/> &#160; <xsl:value-of select="name"/> &#160; <xsl:value-of select="country"/> &#160; <xsl:value-of select="city"/>
        </li>
    </xsl:for-each>
    </ul>
    </body>
</html>
</xsl:template></xsl:stylesheet>
