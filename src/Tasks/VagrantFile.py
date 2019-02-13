# coding: utf-8
from socket import inet_aton

import struct
import os
import re

class VagrantFile():
    def __init__(self, dirName):
        self.dirName = dirName

    def showInUse(self):
        ports = list(set(self.getPortNumbers()))
        ports = sorted(ports)

        publicIps = list(set(self.getPublicIps()))
        publicIps = sorted(publicIps, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])

        privateIPs = list(set(self.getPrivateIps()))
        privateIPs = sorted(privateIPs, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])

        portsString = '# Port number in use\n'
        portsString += self.listToString(ports)
        
        publicIpsString = '# Public IP address in use\n'
        publicIpsString += self.listToString(publicIps)

        privateIPsString = '# Private IP address in use\n'
        privateIPsString += self.listToString(privateIPs)

        return '{}\n{}\n{}\n'.format(portsString, publicIpsString, privateIPsString)
        
        
    def listToString(self, list):
        if not list: return '- None\n'

        concatenatedString = ''
        for item in list:
            concatenatedString += '- {}\n'.format(item)
        return concatenatedString


    def getPortNumbers(self):
        portNumberList = []
        files = self.getFiles()
        for file in files:
            portNumberIncludedLines = self.getPortIncludedLines(file)
            if portNumberIncludedLines is None: continue
            
            for portNumberIncludedLine in portNumberIncludedLines:
                portNumberList.append(self.extractPortNumber(portNumberIncludedLine))
        
        return portNumberList


    def getPublicIps(self):
        publicIpList = []
        files = self.getFiles()
        for file in files:
            publicIpIncludedLines = self.getIpIncludedLines(file, 'public')
            if publicIpIncludedLines is None: continue
            
            for publicIpIncludedLine in publicIpIncludedLines:
                publicIpList.append(self.extractIp(publicIpIncludedLine))
        
        return publicIpList


    def getPrivateIps(self):
        privateIpList = []
        files = self.getFiles()
        for file in files:
            privateIpIncludedLines = self.getIpIncludedLines(file, 'private')
            if privateIpIncludedLines is None: continue
            
            for privateIpIncludedLine in privateIpIncludedLines:
                privateIpList.append(self.extractIp(privateIpIncludedLine))
        
        return privateIpList


    def getPortIncludedLines(self, file):
        portIncludedLines = []
        portPattern = re.compile('forwarded_port')
        
        f = open(file, 'r')
        lines = f.readlines()
        for line in lines:
            # ignore line does not include forwarded_port
            if not portPattern.search(line): continue
            
            # ignore comment
            splitedLine = line.split()
            if splitedLine[0] == '#': continue
            
            portIncludedLines.append(line)
        f.close()

        return portIncludedLines


    def getIpIncludedLines(self, file, type):
        ipIncludedLines = []
        IpPattern = re.compile('public_network')
        if type is 'private':
            IpPattern = re.compile('private_network')

        f = open(file, 'r')
        lines = f.readlines()
        for line in lines:
            # ignore line does not include forwarded_port
            if not IpPattern.search(line): continue
            
            # ignore comment
            splitedLine = line.split()
            if splitedLine[0] == '#': continue
            
            ipIncludedLines.append(line)
        f.close()

        return ipIncludedLines


    def extractIp(self, ipIncludedLine):
        rightOfIp = ipIncludedLine.split('ip')[1]
        rightOfColon = rightOfIp.split(':')[1]
        leftOfComma = rightOfColon.split(',')[0]
        erasedQuotations = leftOfComma.replace("'", '').replace('"', '')

        return erasedQuotations.strip()


    def extractPortNumber(self, portNumberIncludedLine):
        rightOfHost = portNumberIncludedLine.split('host')[1]
        rightOfColon = rightOfHost.split(':')[1]
        leftOfComma = rightOfColon.split(',')[0]

        return leftOfComma.strip()

    def getFiles(self):
        vagrantFiles = []
        for (path, dir, files) in os.walk(self.dirName):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if filename == 'Vagrantfile':
                    vagrantFiles.append('{}\\{}'.format(path, filename))

        return vagrantFiles